import midiutil
from flask import Flask, render_template, request, redirect, send_from_directory, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
output_folder = "E:/code/python/midi/static/midi"
output_path = f"{output_folder}/my_midi_file.mid"



# render the index page with a form to get user input
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # get user input from the form
        chords_str = request.form['chords']
        tempo = int(request.form['tempo'])
        duration = float(request.form['duration'])
        track = int(request.form['track'])

        # process the user input and generate the MIDI file
        chord_map = {
            "c": [48, 52, 55],
    "c#": [49, 53, 56],
    "d": [50, 54, 57],
    "d#": [51, 55, 58],
    "e": [52, 56, 59],
    "f": [53, 57, 60],
    "f#": [54, 58, 61],
    "g": [55, 59, 62],
    "g#": [56, 60, 63],
    "a": [57, 61, 64],
    "a#": [58, 62, 65],
    "b": [59, 63, 66],
    "cm": [48, 51, 55],
    "c#m": [49, 52, 56],
    "dm": [50, 53, 57],
    "d#m": [51, 54, 58],
    "em": [52, 55, 59],
    "fm": [53, 56, 60],
    "f#m": [54, 57, 61],
    "gm": [55, 58, 62],
    "g#m": [56, 59, 63],
    "am": [57, 60, 64],
    "a#m": [58, 61, 65],
    "bm": [59, 62, 66],
    "csus2": [48, 51, 58],
    "dsus2": [50, 53, 60],
    "esus2": [52, 55, 62],
    "fsus2": [53, 56, 63],
    "gsus2": [55, 58, 65],
    "asus2": [57, 60, 67],
    "csus4": [48, 51, 56],
    "dsus4": [50, 53, 58],
    "esus4": [52, 55, 60],
    "fsus4": [53, 56, 61],
    "gsus4": [55, 58, 63],
    "asus4": [57, 60, 65],
            # add more chords to the map as needed
        }
        chords_list = chords_str.lower().split()
        midifile = midiutil.MIDIFile(1)
        midifile.addTempo(track, 0, tempo)
        time = 0
        for chord_name in chords_list:
            if chord_name in chord_map:
                notes = chord_map[chord_name]
                for note in notes:
                    midifile.addNote(0, track, note, time, duration, 100)
                time += duration
            else:
                print(f"Invalid chord: {chord_name}")
        with open(output_path, "wb") as output_file:
          midifile.writeFile(output_file)

        return 'MIDI file generated!'
    else:
        return render_template('home.html')

@app.route('/midi/<filename>')
def serve_midi(filename):
    return send_from_directory(app.static_folder + '/midi', filename)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

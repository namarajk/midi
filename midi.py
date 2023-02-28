from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "John"
    return render_template('index.html', name=name)
    
import midiutil


# map chord names to MIDI note numbers
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
}

# get user input for chords
chords_str = input("Enter chords (separated by spaces): ")
chords_list = chords_str.lower().split()

# get user input for tempo, duration, and track
tempo = int(input("Enter tempo (BPM): "))
duration = float(input("Enter duration of each chord (in seconds): "))
track = int(input("Enter MIDI track number: "))

# create MIDI file with one track
midifile = midiutil.MIDIFile(1)

# set tempo
midifile.addTempo(track, 0, tempo)

# add notes for each chord
time = 0
for chord_name in chords_list:
    if chord_name in chord_map:
        notes = chord_map[chord_name]
        for note in notes:
            midifile.addNote(0, track, note, time, duration, 100)
        time += duration
    else:
        print(f"Invalid chord: {chord_name}")

# write MIDI file
with open("output.mid", "wb") as output_file:
    midifile.writeFile(output_file)

## Extracting pitch only

import os
import shutil
import copy
import mido
from mido import MidiFile

# def get_note(msg):
#     dict = msg.dict()
#     if 'velocity' in dict.keys() and dict['velocity'] != 0 and 'note' in dict.keys():
#         note_seq = dict['note']
#         # print(note_seq)
#         return note_seq

mid_files_path = 'schubert_lieder'
test_mid = MidiFile('schubert_lieder/ImWunderschonenMonatMai.mid')



for file_name in os.listdir('schubert_lieder'):
    notes_seq = []
    if '.mid' in file_name:
        full_path = 'schubert_lieder/' + file_name
        mid = MidiFile(full_path)

        #Get Track 1 Vocal only, and pitch only:
        vocal_track = mid.tracks[1]
        for msg in vocal_track:
            dict = msg.dict()
            if 'velocity' in dict.keys() and dict['velocity'] != 0 and 'note' in dict.keys():
                note_seq = dict['note']
                notes_seq.append(str(note_seq))
                # note_seq = str(note_seq)
                # print(note_seq)

    notes_seq = ' '.join(notes_seq)


if __name__ == '__main__':
    # write notes to text file
    note_file = open("./miditext/input_schubert.txt", "w")
    note_file.write(notes_seq)
    note_file.close()

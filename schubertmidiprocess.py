import os
import mido
from mido import MidiFile


for file_name in os.listdir('./schubert_midi'):
	if '.mid' in file_name:
		# print file_name
		full_path = './schubert_midi/' + file_name
		# print full_path

		mid = MidiFile(full_path)

	# look at the track names
	for i, track in enumerate(mid.tracks):
		print((i, track.name))
		#track1 = righthand, track2 = lefthand

	# create array of notes
	notes = []
	messages = []

	#righthand-notes and time only
	for message in mid.tracks[1]:
	    messages.append(message)

	for m in range(len(messages)):
	    # print messages[m]
	    note = ""
	    time = ""
	    if messages[m].type == 'note_on':
	        message_components = str(messages[m]).split(' ')
	        for item in message_components:
	            if 'note=' in item:
	                # notes.append(item.split('note=')[1])
	                note = item.split('note=')[1]
	        message_components = str(messages[m+1]).split(' ')
	        for item in message_components:
	            if 'time=' in item:
	                time = item.split('time=')[1]
	    if note != "":
	        notes.append(str(note + "_" + time))


	notes = ' '.join(notes)
	#print notes



#write notes to text file
note_file = open("../python2_music_lstm/miditext/input_schubert.txt", "w")
note_file.write(notes)
note_file.close()








#--------------------------------------------------------------------------

		# #create array of notes
		#
		# notes = []
		# for message in mid.tracks[1]: #righthand notes-only
		#     #print message
		#     if message.type == 'note_on':
		#         message_components = str(message).split(' ')
		#
		# 	    for item in message_components:
		#             if 'note=' in item:
		#                 notes.append(item.split('note=')[1])
		#
		# 		for item in message_components:
        #     		if 'time=' in item:
        #         		time = item.split('time=')[1]
		#
		# 	if note != "":
        # 		notes.append(str(note + "_" + time))
		#
		#
		# notes = ' '.join(notes)
		#
		# print notes


		# #write notes to text file
		# note_file = open("../miditext/notes.txt", "w")
		# note_file.write(notes)
		# note_file.close()

import os
import mido
from mido import MidiFile


for file_name in os.listdir('schubert_lieder'):
	if '.mid' in file_name:
		# print file_name
		full_path = './schubert_lieder/' + file_name
		print('==========================================================')
		print(full_path)

		mid = MidiFile(full_path)

	# create array of notes
	notes = []
	messages = []

	#righthand-notes and time only
	for message in mid.tracks[1]:
		# track1 = righthand, track2 = lefthand
		messages.append(message)

	for m in range(len(messages)):
		print(messages[m])
		note = ""
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

		if note != "" and time!=0:
			notes.append(str(note + "_" + time))

	notes = ' '.join(notes)
	#print(notes)


if __name__ == '__main__':
	#write notes to text file
	note_file = open("./miditext/input_schubert.txt", "w")
	note_file.write(notes)
	note_file.close()







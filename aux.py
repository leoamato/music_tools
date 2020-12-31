#DATES

notes = ["C", "C#", "D", "D#", "E", "F", 
         "F#", "G", "G#", "A", "A#", "B"]

intervals = ["Unisono", "2m", "2M", "3m", "3M", "4j", 
			 "5dim", "5j", "6m", "6M", "7m", "7M", "8j"]

#AUXILIAR FUNCTIONS

# ENHARMONY

def have_bemol (note):
	if (len (note) == 2):
		alteration = note[1]
		if (alteration == 'b'):
			return True

	return False

def enharmony (note):
	index_note = search_note (note)
	return (index_note - 1)

def check_enharmony(note):
	if (have_bemol (note)):
		return (notes[enharmony (note[0])])

	return note

# ----------

# TO DATA TYPES

def search_interval (interval):
	index = 0

	while (intervals[index] != interval):
		index += 1

	return (index)

def search_note (note):
	index = 0

	while (notes[index] != note):
		if (index > 11):
			index = 0

		index += 1

	return index

def distance (note1, note2):
	value1 = search_note(note1)
	value2 = search_note(note2)

	if (value1 < value2):
		return (value2 - value1)

	elif (value1 > value2):
		return (value1 - value2)

	else:
		print ("Something are wrong!")
		return 0

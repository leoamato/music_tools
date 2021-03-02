# Import aux funtions

from aux import have_bemol
from aux import enharmony
from aux import check_enharmony
from aux import search_interval
from aux import search_note
from aux import distance

#DATES

notes = ["C", "C#", "D", "D#", "E", "F", 
         "F#", "G", "G#", "A", "A#", "B"]

intervals = ["Unisono", "2m", "2M", "3m", "3M", "4j", 
			 "5dim", "5j", "6m", "6M", "7m", "7M", "8j"]

# INTERVALS FUNCTIONS

def intervals_calculator (base, interval, sense):
	index = search_note(base)
	offset = search_interval (interval)
	result = 0

	if (offset == 0 or offset == 12):
		result = index

	if (sense == "asc" and index + offset < 12):
		result = index + offset

	elif (sense == "asc" and index + offset >= 12):
		result = abs (12 - (index + offset))

	elif (sense == "dec" and index - offset >= 0):
		result = index - offset

	else:
		result = 12 + (index - offset)

	assert (0 <= result and result < 12)

	return notes[result]

def tell_interval (base, dest, sense):
	base_n = search_note (base)
	dest_n = search_note (dest)
	interv = 0

	if (base_n == dest_n):
		return intervals[12]

	elif (sense == "asc" and base_n < dest_n):
		interv = (dest_n - base_n)

	elif (sense == "asc" and base_n > dest_n):
		interv = (12 - base_n) + dest_n

	elif (sense == "dec" and base_n < dest_n):
		interv = (12 - dest_n) + base_n

	else:
		interv = (base_n - dest_n);

	assert(0 <= interv and interv <= 12)

	return intervals[interv]

# ----------

#CHORDS FUNCTIONS

def tell_3chord (root, third, fift):
	newroot = check_enharmony (root)
	newthird = check_enharmony (third)
	newfift = check_enharmony (fift)

	dist1 = tell_interval(newroot, newthird, "asc")
	dist2 = tell_interval(newthird, newfift, "asc")

	if (dist1 == "3M" and dist2 == "3m"):
		chord = root

	elif (dist1 == "3m" and dist2 == "3M"):
		chord = root+'m'

	elif (dist1 == "3m" and dist2 == "3m"):
		chord = root + ' Dim'

	elif (dist1 == "3M" and dist2 == "3M"):
		chord = root + ' Aum'

	else :
		print ("Something are wrong!")
		return "0"

	return chord

def build_3chord (chord, chord_type):

	if (chord_type == "M"):
		root = chord
		third = intervals_calculator (chord, "3M", "asc")
		fift = intervals_calculator (chord, "5j", "asc")
		final_chord = [root, third, fift]

	elif (chord_type == "m"):
		root = chord
		third = intervals_calculator (chord, "3m", "asc")
		fift = intervals_calculator (chord, "5j", "asc")
		final_chord = [root, third, fift]

	elif (chord_type == "dim"):
		root = chord
		third = intervals_calculator (chord, "3m", "asc")
		fift = intervals_calculator (chord, "5dim", "asc")
		final_chord = [root, third, fift]

	elif (chord_type == "aum"):
		root = chord
		third = intervals_calculator (chord, "3M", "asc")
		fift = intervals_calculator (chord, "6m", "asc")
		final_chord = [root, third, fift]

	else:
		print ("Something are wrong!")
		return 0

	return final_chord

def tell_4chord (root, third, fift, seven):
	newroot = check_enharmony (root)
	newthird = check_enharmony (third)
	newfift = check_enharmony (fift)
	newseven = check_enharmony (seven)
	chord = root

	thriad = tell_3chord(newroot, newthird, newfift)
	seven_distance = tell_interval(newroot, newseven, "asc")
	
	if (thriad == (root) and seven_distance == "7M"):
		chord = root + 'Maj7'

	elif (thriad == (root) and seven_distance == "7m"):
		chord = root + '7'

	elif (thriad == (root + 'm') and seven_distance == "7m"):
		chord = root + 'm7'

	elif (thriad == (root + ' Dim') and seven_distance == "7m"):
		chord = root + ' m7b5'

	else:
		print ("Error parsing chord!")
		return 0

	return chord

def build_4chord (chord, chord_type):

	if (chord_type == "Maj7"):
		root = chord
		third = intervals_calculator (chord, "3M", "asc")
		fift = intervals_calculator (chord, "5j", "asc")
		seven = intervals_calculator (chord, "7M", "asc")
		final_chord = [root, third, fift, seven]

	elif (chord_type == "7"):
		root = chord
		third = intervals_calculator (chord, "3M", "asc")
		fift = intervals_calculator (chord, "5j", "asc")
		seven = intervals_calculator (chord, "7m", "asc")
		final_chord = [root, third, fift, seven]

	elif (chord_type == "m7"):
		root = chord
		third = intervals_calculator (chord, "3m", "asc")
		fift = intervals_calculator (chord, "5j", "asc")
		seven = intervals_calculator (chord, "7m", "asc")
		final_chord = [root, third, fift, seven]

	elif (chord_type == "m7b5"):
		root = chord
		third = intervals_calculator (chord, "3m", "asc")
		fift = intervals_calculator (chord, "5dim", "asc")
		seven = intervals_calculator (chord, "7m", "asc")
		final_chord = [root, third, fift, seven]

	else:
		print ("Something are wrong!")
		return 0

	return final_chord


"""
def create_scale (note, scale_type):



"""

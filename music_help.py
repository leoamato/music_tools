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

	dist1 = distance (newroot, newthird)
	dist2 = distance (newthird, newfift)

	if (dist1 == 4 and dist2 == 3):
		chord = root

	elif (dist1 == 3 and dist2 == 4):
		chord = root+'m'

	elif (dist1 == 3 and dist2 == 3):
		chord = root + ' Dim'

	elif (dist1 == 4 and dist2 == 4):
		chord = root + ' Aum'

	else :
		print ("Something are wrong!")
		return "0"

	return chord

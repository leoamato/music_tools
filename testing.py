
notes = ["C", "C#", "D", "D#", "E", "F", 
         "F#", "G", "G#", "A", "A#", "B"]

intervals = ["Unisono", "2m", "2M", "3m", "3M", "4j", 
			 "5dim", "5j", "6m", "6M", "7m", "7M", "8j"]

# Testing interval functions

from music_help import intervals_calculator
from music_help import tell_interval
from music_help import tell_3chord
from music_help import build_3chord
from music_help import tell_4chord
from music_help import build_4chord

hit = 0
miss = 0

for i in range (0,12):
	for j in range (0,13):
		
		result = intervals_calculator (notes[i], intervals[j], "dec")
		expected = tell_interval (notes[i], result, "dec")


		if (expected == intervals[j]):
			hit += 1
		else:
			miss += 1

print ("hits", hit)
print ("misses", miss)

# ----------------------------------------------------------------------------------------------
# Test triad chords

hit = 0
miss = 0

print "Testing Mayor chords"
for i in range (0,12):
	third = intervals_calculator (notes[i], "3M", "asc")
	fift = intervals_calculator (notes[i], "5j", "asc")

	test1 = tell_3chord(notes[i], third, fift)
	test2 = build_3chord (notes[i], "M")

	if (test2[0] == notes[i] and test2[1] == third and test2[2] == fift):
		hit += 1
	else :
		miss += 1

print ("hits", hit)
print ("misses", miss)

# ----------

hit = 0
miss = 0

print "Testing minor chords"
for i in range (0,12):
	third = intervals_calculator (notes[i], "3m", "asc")
	fift = intervals_calculator (notes[i], "5j", "asc")

	test1 = tell_3chord(notes[i], third, fift)
	test2 = build_3chord (notes[i], "m")

	if (test2[0] == notes[i] and test2[1] == third and test2[2] == fift):
		hit += 1
	else :
		miss += 1

print ("hits", hit)
print ("misses", miss)

# ----------

hit = 0
miss = 0

print "Testing dim chords"
for i in range (0,12):
	third = intervals_calculator (notes[i], "3m", "asc")
	fift = intervals_calculator (notes[i], "5dim", "asc")

	test1 = tell_3chord(notes[i], third, fift)
	test2 = build_3chord (notes[i], "dim")

	if (test2[0] == notes[i] and test2[1] == third and test2[2] == fift):
		hit += 1
	else :
		miss += 1

print ("hits", hit)
print ("misses", miss)

# ----------

hit = 0
miss = 0

print "Testing aum chords"
for i in range (0,12):
	third = intervals_calculator (notes[i], "3M", "asc")
	fift = intervals_calculator (notes[i], "6m", "asc")

	test1 = tell_3chord(notes[i], third, fift)
	test2 = build_3chord (notes[i], "aum")

	if (test2[0] == notes[i] and test2[1] == third and test2[2] == fift):
		hit += 1
	else :
		miss += 1

print ("hits", hit)
print ("misses", miss)

print "------"
# ----------------------------------------------------------------------------------------------
# Test quad chords

hit = 0
miss = 0

print "Testing Maj7 chords"
for i in range (0,12):
	third = intervals_calculator (notes[i], "3M", "asc")
	fift = intervals_calculator (notes[i], "5j", "asc")
	seven = intervals_calculator (notes[i], "7M", "asc")

	test1 = tell_4chord(notes[i], third, fift, seven)
	test2 = build_4chord (notes[i], "Maj7")

	if (test2[0] == notes[i] and test2[1] == third and test2[2] == fift and test2[3] == seven):
		hit += 1
	else :
		miss += 1

print ("hits", hit)
print ("misses", miss)

# ----------

hit = 0
miss = 0

print "Testing m7 chords"
for i in range (0,12):
	third = intervals_calculator (notes[i], "3m", "asc")
	fift = intervals_calculator (notes[i], "5j", "asc")
	seven = intervals_calculator (notes[i], "7m", "asc")

	test1 = tell_4chord(notes[i], third, fift, seven)
	test2 = build_4chord (notes[i], "m7")

	if (test2[0] == notes[i] and test2[1] == third and test2[2] == fift and test2[3] == seven):
		hit += 1
	else :
		miss += 1

print ("hits", hit)
print ("misses", miss)

# ----------

hit = 0
miss = 0

print "Testing 7 chords"
for i in range (0,12):
	third = intervals_calculator (notes[i], "3M", "asc")
	fift = intervals_calculator (notes[i], "5j", "asc")
	seven = intervals_calculator (notes[i], "7m", "asc")

	test1 = tell_4chord(notes[i], third, fift, seven)
	test2 = build_4chord (notes[i], "7")

	if (test2[0] == notes[i] and test2[1] == third and test2[2] == fift and test2[3] == seven):
		hit += 1
	else :
		miss += 1

print ("hits", hit)
print ("misses", miss)

# ----------

hit = 0
miss = 0

print "Testing m7b5 chords"
for i in range (0,12):
	third = intervals_calculator (notes[i], "3m", "asc")
	fift = intervals_calculator (notes[i], "5dim", "asc")
	seven = intervals_calculator (notes[i], "7m", "asc")

	test1 = tell_4chord(notes[i], third, fift, seven)
	test2 = build_4chord (notes[i], "m7b5")

	if (test2[0] == notes[i] and test2[1] == third and test2[2] == fift and test2[3] == seven):
		hit += 1
	else :
		miss += 1

print ("hits", hit)
print ("misses", miss)


#Import functions music_help.py

from music_help import intervals_calculator
from music_help import tell_interval
from music_help import tell_3chord
from music_help import build_3chord
from music_help import tell_4chord
from music_help import build_4chord

# MAIN PROGRAM
loop = 1
while (loop == 1):
	
	print "********** MUSIC TOOLS **********\n"

	print "Main menu\n"

	print "1) Calculates intervals"
	print "2) Comprovate interval"
	print "3) Calculates a thriad chord"
	print "4) Comprovate a thriad chord"
	print "5) Calculates a quad chord"
	print "6) Comprovate a quad chord"
	print 

	selection = input ()

	if (selection == 1): # Interval calculator

		note = str(raw_input ("Please insert a note \n"))
		interval = str(raw_input ("Please insert a interval\n"))
		sense = str(raw_input ("Please insert a sense\n"))

		result = intervals_calculator (note, interval, sense)
		print(result)

	elif (selection == 2): # Tell interval

		note1 = str(raw_input ("Please insert a note \n"))
		note2 = str(raw_input ("Please another note\n"))
		sense = str(raw_input ("Please insert a sense\n"))

		result = tell_interval (note1, note2, sense)
		print(result)

	elif (selection == 3): #Tell thriad chord

		chord = str(raw_input ("Please insert a chord \n"))
		chordtype = str(raw_input ("Please insert a chord type (M, m, aum, dim)\n"))

		result = build_3chord(chord, chordtype)
		print (result)

	elif (selection == 4): #Create thriad chord

		rootnote = str(raw_input ("Please insert the root note \n"))
		thirdnote = str(raw_input ("Please insert the third \n"))
		fifnote = str(raw_input ("Please insert the fift \n"))

		result = tell_3chord (rootnote, thirdnote, fifnote)
		print (result)

	elif (selection == 5): #Tell quad chord

		chord = str(raw_input ("Please insert a chord \n"))
		chordtype = str(raw_input ("Please insert a chord type (Maj7, 7, m7, m7b5)\n"))

		result = build_4chord(chord, chordtype)
		print (result)

	elif (selection == 6): #Create quad chord

		rootnote = str(raw_input ("Please insert the root note \n"))
		thirdnote = str(raw_input ("Please insert the third \n"))
		fifnote = str(raw_input ("Please insert the fift \n"))
		sevenote = str(raw_input ("Please insert the seven \n"))

		result = tell_4chord (rootnote, thirdnote, fifnote, sevenote)
		print (result)

	else:
		print ("Something are wrong, please enter a correct number")

	print ("Sorry for enharmony errors :P ")

	print ("do you want to do another task?\n")
	print ("1_ Yes")
	print ("2_ No")

	loop = input ()


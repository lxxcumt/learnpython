print "You enter a dark room with two doors,. do you through door #1 or door #2?"

door =raw_input("> ")

if door=="1":
	print "there is a giant bear eating cake. what do you do?"
	print "1. take the cake."
	print "2. scream at the bear."
	
	bear=raw_input("> ")
	
	if bear=="1":
		print "the bear eats your face off. Good job!"
	elif bear=="2":
		print "the bear eats your leg off. Good job!"
	else:
		print "well, doing %s is probably better. Bear runs away."% bear

elif  door=="2":
	print "you stare into the endless abyss at Cthulu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity =raw_input("> ")
	
	if insanity=="1" or insanity=="2":
		print "your body survives powered by a mind of jello. Good job!"
	else:
		print "the insanity rots your eyes into a pool of muck. Good job!"
	
else:
	print "you stumble around and fall on a knife and die. Good job!"

people=30
cars=40
buses=15


if cars>people:
	print "We should take the cars."
elif cars<people:
	print  "we should not take the cars."
else:
	print "We can't decide."

if buses>cars:
	print "That's too many buses."
elif buses<cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

if people>cars:
	print "alright, let's just take buses."
else:
	print "Fine, let's just stay home then."
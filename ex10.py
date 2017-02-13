tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\a\\cat."
cat_number = 32

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print "This is a \u3232."

print "I have %x cats." %cat_number

print '''
I like to have
\t& a cat
\t& a dog
\t& a fish
\t& a monkey
'''

Longyangroad = "LONGYANG STATION is the Node of \n2\\\n7\\\n16\\\r\nlines."

print Longyangroad

# see the difference between "\n" and "\r".
print """
AAAAAAAAAAAAAA\nBBBBBB

AAAAAAAAAAAAAA\rBBBBBB
"""
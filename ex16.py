s = "This is good."
repr(s)
print s 
print type(s)

print str(1/7)

print "this very good \\\n YES, IT IS."
# str.format
print 'We are the {} who says "{}!"'.format('Knights', 'Ni')
# str.format
print '12'.zfill(10)
print '-3.1415926'.zfill(11)

# the following code is for ex16

from sys import argv

script, filename = argv

print "We are going to erase %r." %filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you don't want that, hit RETURN."

raw_input("?")

print "opening the file...."
target =open(filename,'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print "And finally, we close it."
target.close()

target = open(filename)

print target.read()

line4 = "I'm looking for summer vibe."
target = open(filename, 'a') # Use mode 'a' (Not 'w') to add content to the end of existed content and will not overite the existed conten
target.write(line4)


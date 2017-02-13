from sys import argv
from os.path import exists

script, from_file, to_file =argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata) # len: return the length of an object

print "Does the output file exist? %r" %exists(to_file) # exists: Return True if path refers to an existing path
print "Ready, hit RETURN to continue, CTRL--C to abort."
raw_input

outfile = open(to_file,'w')
outfile.write(indata)

print "Alright, all done."

outfile.close()
in_file.close()


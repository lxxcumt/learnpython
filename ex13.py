from sys import argv

script, first, second, third = argv

print argv

print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "This is good."

first = raw_input()
second = raw_input()
third = raw_input()

print first, second, third, script
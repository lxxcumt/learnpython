x = "There are %d types of people." % 10 # define x
binary = "binary" #define binary
do_not = "don't" #define do_not
y = "Those who know %s and those who %s." % (binary, do_not) #define y

print x
print y

print "I said: %r." % x
print "I also said : '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation %hilarious

w = "There is the left side of ..."
e = "a string with a right side"

print w+e
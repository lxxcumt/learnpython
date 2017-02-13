from sys import argv

script, user_name, Job_title = argv
prompt = '==> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions, are you a %s?" %(Job_title)
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "What do you work for?"
Company_name = raw_input(prompt)

print """
Alright, so you said %r about liking me.
YOu live in %r. Not sure where that is.
And you have a %r computer. And you work for %s. Nice.
""" % (likes, lives, computer, Company_name)

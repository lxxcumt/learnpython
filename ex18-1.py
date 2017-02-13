from sys import argv

script, filename = argv # In this step, the file has been created.

test_txt = open(filename, 'w')
txt = raw_input("Please write what you want to say to her.")

print test_txt.write(txt)

test_txt.close
# define the function 
def function_while(num,numb,numbers,increment):
	while num<numb:
		print "At the top num is %d" % num
		numbers.append(num)
		num = num + increment
		print "numbers now:", numbers
		print "At the bottom num is %d" % num

num =int(raw_input("please enter a num: "))
numb =int(raw_input("please enter a numb: "))
increment =int(raw_input("please enter the increment:"))
numbers = []

function_while(num, numb,numbers, increment)
	
print "The numbers:"

for num in numbers:
	print num
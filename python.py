# print all the numbers from 1-1000
# for x in range(1000):
# 	print x

# print all the multiples of 5 equal to or less than 1000
# x = 0
# while x <= 1000:
# 	print x
# 	x += 5

#print a sum of all the values in the list
# a = [1, 2, 5, 10, 255, 3]
# answer = 0
# for x in a:
# 	answer += x
# print answer

# print the average of the list
# a = [1, 2, 5, 10, 255, 3]
# answer = 0
# for x in a:
# 	answer += x
# print answer/len(a)

# print out numbers 1-2000 and if they're odd or even
# for x in range(2000):
# 	if x % 2 == 0:
# 		print "The number " + str(x) + " is an even number!"
# 	else:
# 		print "The number " + str(x) + " is an odd number!"

#
# for i in range(2):
# 	grade = raw_input("Give me a test score")

# 	print grade

# 	if grade >= '90':
# 		print "You got an A!"
# 	elif grade >= '80':
# 		print "You got a B!"
# 	elif grade >= '70':
# 		print "You got a C!"
# 	elif grade >= '60':
# 		print "You got a D!"
# 	else:
# 		print "You suck"


# multiply all items in list by a number
a = [4,6,5,2,3]

def multiply(x,c):
	for i in range(len(x)):
		x[i] = x[i] * c
	return x

b = multiply(a,5)
print b











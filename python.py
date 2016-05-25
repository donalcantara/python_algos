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
for x in range(2000):
	if x % 2 == 0:
		print "The number " + str(x) + " is an even number!"
	else:
		print "The number " + str(x) + " is an odd number!"
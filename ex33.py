i = 0
numbers = []
booty = 20

while i < booty:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 2
	
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
print "The numbers: "

for num in numbers:
	print num
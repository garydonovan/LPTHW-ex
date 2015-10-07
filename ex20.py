
# imports sys module
from sys import argv


# Parameter for command line input
script, input_file = argv

# Defines the function print_all with one argument which reads that argument
def print_all(f):
	print f.read()

# Defines the rewind function which takes argument f
def rewind(f):
	f.seek(0)

# Defines function print_a_line with two parameters, prints the first and reads just one line of the second
def print_a_line(line_count, f):
	print line_count, f.readline()
	
# Sets a variable to open command line argument	
current_file = open(input_file)

# Print statement
print "First let's print the whole file:\n"

# Calls method print_all with argument to open file
print_all(current_file)

# Calls function rewind with method .seek which read file starting from the start hence "0"
print "Now let's rewind, kind of like a tape."
rewind(current_file)

# Print statement
print "Let's print three lines:"

# Runs script three times setting variable current_line to be passed into print_a_line as an argument
# Like a manual loop

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
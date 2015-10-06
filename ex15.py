# This program is for reading files

# This line imports argument vector from system module
from sys import argv

# These are the arguments that argv takes, script is default
script, tits = argv

# Create variable which opens file
txt = open(tits)

# Print that filename and print text of the file using read append
print "Here's your file %r:" % tits
print txt.read()
txt.close()

# Create a user defined variable in form of filename
print "Type the filename again:"
file_again = raw_input("> ")

# Assigns and opens the file defined by user
txt_again = open(file_again)

# Prints to the terminal content of file

print txt_again.read()
txt_again.read()
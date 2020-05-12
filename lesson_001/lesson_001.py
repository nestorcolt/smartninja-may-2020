"""

Resources:
    https://docs.python.org/3/library/functions.html  (Python built-in functions)

"""

##############################################################################################
# Class 001
# Variables

x = 5
y = 2

# Result
print(x + y)  # Should be 12

# More than numbers:
some_string = "Hey there!"
other_string = 'Hey there!'

print(some_string)
print(other_string)

# Booleans
bool_one = True
bool_two = False

print(bool_one)

# None
some_var = None
print("First Definition of some_var: ", some_var)

##############################################################################################
# Redefining a variable
some_var = 14
print("Second Definition of some_var: ", some_var)

##############################################################################################
# Comments

# this is a comment (This is and in-line comment)
# Block comment section

"""

This is a block of comment tha can be split 
in multiple lines or block of lines. 

"""

print(""" print this to the console """)

##############################################################################################
# User input
user_name = input("Please enter your name: ")
greeting = "Hello " + user_name + "!"  # concatenation
print(greeting)

##############################################################################################

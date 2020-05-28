from functions import greetings, count_to_100


##############################################################################################
# Definition of a function

def say_hello():
    print("Hello!")


# Function call
# say_hello()

##############################################################################################
# Reusability ??
"""
say_hello()
say_hello()
say_hello()
say_hello()
say_hello()
say_hello()
say_hello()
say_hello()
say_hello()
say_hello()
say_hello()
say_hello()
"""


##############################################################################################
# import a function
# greetings()
# count_to_100()

##############################################################################################
def say_hello_2(name):
    print("Hello {0}!".format(name))


# say_hello_2(name="Nestor")
##############################################################################################

def say_hello_3(name):
    return "Hello {0}!".format(name)


greeting = say_hello_3(name="Nestor")


# print(greeting)

##############################################################################################
# Homework
# Calculate the sum of 2 numbers with a function

def calculate_sum(num_a, num_b):
    result = int(num_a) + int(num_b)
    return result


result = calculate_sum(5, 50)


# print(result)

# Calculate the cube of a number
def cube_of_x(number):
    return number * number * number


result = cube_of_x(5)


# print(result)

# Difference of a numbers
def abs_difference_of_x(num_a, num_b):
    result = abs(num_a - num_b)
    return result


result = abs_difference_of_x(5, 10)
# print(result)

##############################################################################################
# BONUS
# String operations
"""
    String are not mutable data types
"""

"""
    Resources
    https://www.w3schools.com/python/python_ref_string.asp


"""

a_string = "This is a Python course"

# upper
print(a_string.upper())

# Index of
print(a_string.index("o"))

# count
print(a_string.count("s"))

# split
print(a_string.split(" "))

# zfill
print("1".zfill(3))

##############################################################################################

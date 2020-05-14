import random

# Guess the secret number INIT

##############################################################################################

secret = 22
guess = 0

"""

while guess != secret:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You guessed it - congratulations! It's number 22.")
    else:
        print("Sorry, your guess is not correct... The secret number is not " + str(guess))

"""

##############################################################################################
# For loop
secret = 22

demo_list = [0, 1, 2, 3, 4]

"""
for x in demo_list:
    print("Element in iteration: ", x)
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You've guessed it - congratulations! It's number 22.")
        break
    else:
        print("Sorry, your guess is not correct... The secret number is not " + str(guess))
"""

##############################################################################################
# While with break
secret = 22

"""
while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You've guessed it - congratulations! It's number 22.")
        break

    else:
        print("Sorry, your guess is not correct... The secret number is not " + str(guess))

"""
##############################################################################################
# While with complex conditions
"""
secret = 22

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You've guessed it - congratulations! It's number 22.")
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

"""

##############################################################################################
# Imports in Python
secret = random.randint(1, 30)

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

##############################################################################################

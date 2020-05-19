# Storing data into a TXT file

"""
Resources:
https://bic-berkeley.github.io/psych-214-fall-2016/string_literals.html

"""

path = r"C:\Users\Sudo\Desktop\SmartNinja\Curso 05_2020\msg.txt"

"""
r = show text in raw mode
"""

# Read information from a text file

# Read whole document
with open(path, "r") as ninja_file:
    contents = ninja_file.read()
    # print(contents)

# Read line by line
with open(path, "r") as ninja_file:
    ninja_lines = ninja_file.readlines()

    for line in ninja_lines:
        pass
        # print(line)

# writing information in a txt file
with open("ninja2.txt", "w") as ninja_file_2:
    ninja_file_2.write("Hello, not file! in python")

##############################################################################################
# Guess the secret number

secret = 22
attempts = 0

# Read the stored score before the game and print the output
with open("score.txt", "r") as score:
    best_score = score.read()
    print("The best score in the game: " + best_score)
    print()

# Play
while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        if attempts < int(best_score):
            with open("score.txt", "w") as score_file:
                best_score = score_file.write(str(attempts))

        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

##############################################################################################

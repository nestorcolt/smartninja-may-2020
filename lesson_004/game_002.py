import datetime
import json

##############################################################################################
# Game starts

player = input("Please enter your name: ")

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

# Ordering top scores
list_attemps = []

for element in score_list:
    list_attemps.append(element["attempts"])

list_attemps.sort()
my_filtered_result = list(set(list_attemps))
my_best_players_list = []

for item in score_list:
    stored_attempt = item["attempts"]

    if stored_attempt in my_filtered_result:
        my_best_players_list.append(item)

best_top_3 = my_best_players_list[:3]
print("top 3: {}".format(best_top_3))
##############################################################################################
secret = 22
attempts = 0

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        score_data = {"attempts": attempts,
                      "player": player,
                      "date": str(datetime.datetime.now())}

        score_list.append(score_data)

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        break

    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

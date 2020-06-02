import datetime
import json
import os


##############################################################################################
# Class


class GameEngine:

    def __init__(self):
        pass

    def save_score(self, score_list):
        """
        Saves the score in a json file
        :param score_list: list - This is the score previusly stored or a empty list to star to track scored of the game
        :return:
        """
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

    def read_score(self):
        """
        Read the data from the json file
        :return:
        """
        # Check if path doesn't exist return a empty list (avoid logic crash)
        if not os.path.exists("score_list.txt"):
            return []

        # Otherwise read the data and return the data
        with open("score_list.txt", "r") as score_file:
            score_list = json.loads(score_file.read())
            return score_list

    def show_max_score(self, score_list):
        """
        Parsing a score from a file read and gets the best attemps on the game
        :param score_list: list - This is the score previusly stored or a empty list to star to track scored of the game
        :return:
        """
        # Check if there is not input then return a message with the error
        if not score_list:
            print("Not previous score found")
            return

        # Ordering top scores
        list_attempts = []

        for element in score_list:
            list_attempts.append(element["attempts"])

        list_attempts.sort()
        my_filtered_result = list(set(list_attempts))
        my_best_players_list = []

        for item in score_list:
            stored_attempt = item["attempts"]

            if stored_attempt in my_filtered_result:
                my_best_players_list.append(item)

        best_top_3 = my_best_players_list[:3]
        print("top 3: {}".format(best_top_3))

    def play(self, score_list):
        """
        This functions run the game logic
        :param score_list: list - This is the score previusly stored or a empty list to star to track scored of the game
        :return: None
        """
        player = input("Please enter your name: ")
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
                self.save_score(score_list=score_list)
                break

            elif guess > secret:
                print("Your guess is not correct... try something smaller")
            elif guess < secret:
                print("Your guess is not correct... try something bigger")


##############################################################################################
# Game starts
engine = GameEngine()
score_list = engine.read_score()
engine.show_max_score(score_list)
engine.play(score_list)

##############################################################################################

import datetime
import json
import os


##############################################################################################
# Class


class GameEngine:

    def __init__(self):
        self.attempts = 0

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
        return best_top_3

    def play(self,  guess):
        """
        This functions run the game logic
        :param score_list: list - This is the score previusly stored or a empty list to star to track scored of the game
        :return: None
        """
        secret = 22
        self.attempts += 1
        score_list = self.read_score()

        if guess == secret:
            score_data = {"attempts": self.attempts,
                          "date": str(datetime.datetime.now())}

            score_list.append(score_data)
            self.save_score(score_list=score_list)
            message = self.show_max_score(score_list)
            return message

        elif guess > secret:
            message = "Your guess is not correct... try something smaller"
            return message

        elif guess < secret:
            message = "Your guess is not correct... try something bigger"
            return message

##############################################################################################
# Game starts
# engine = GameEngine()
# score_list = engine.read_score()
# engine.show_max_score(score_list)
# engine.play(score_list)

##############################################################################################

import random


class Game:

    def __init__(self):
        self.player_name = ""
        self.turn = ""

    def test(self, number):
        return number

    def insert_player_game(self, name):
        self.player_name = name
        return self.player_name

    def start_game(self):
        turn = ["Player", "Computer"]
        self.turn = random.choice(turn)
        return self.turn

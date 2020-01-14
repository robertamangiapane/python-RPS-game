import random


class Game:

    def __init__(self):
        self.player_name = ""
        self.players = ["Player", "Computer"]
        self.turn = ""
        self.options = ["Rock", "Paper", "Scissors"]
        self.player_choice = ""
        self.computer_choice = ""

    def insert_player_game(self, name):
        self.player_name = name
        return self.player_name

    def start_game(self):
        self.turn = random.choice(self.players)
        return self.turn

    def player_turn_option(self, choice):
        self.player_choice = choice
        return self.player_choice

    def computer_turn_option(self):
        self.computer_choice = random.choice(self.options)
        return self.computer_choice

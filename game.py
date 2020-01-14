import random


class Game:

    def __init__(self):
        self.player_name = ""
        self.turn = "%s's turn" % self.player_name
        self.players = ["Player", "Computer"]
        self.options = ["Rock", "Paper", "Scissors"]
        self.player_choice = ""
        self.computer_choice = ""
        self.winner = ""

    def insert_player_game(self, name):
        self.player_name = name

        return self.player_name

    def switch_turn(self):
        if self.turn != "Computer's turn":
            self.turn = "Computer's turn"
        else:
            self.turn = "%s's turn" % self.player_name

        return self.turn

    def player_turn_option(self, choice):
        self.player_choice = choice
        self.switch_turn()

        return self.player_choice

    def computer_turn_option(self):
        self.computer_choice = random.choice(self.options)
        self.switch_turn()

        return self.computer_choice

    def declare_winner(self):

        if self.player_choice == self.computer_choice:
            self.winner = "It's a tie!"
        elif self.player_choice == "Paper" and self.computer_choice == "Rock" or\
                self.player_choice == "Rock" and self.computer_choice == "Scissors" or\
                self.player_choice == "Scissors" and self.computer_choice == "Paper":
            self.winner = "%s win!" % self.player_name
        else:
            self.winner = "Computer win!"

        return self.winner

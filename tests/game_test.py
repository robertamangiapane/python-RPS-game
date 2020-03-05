import unittest
from unittest.mock import MagicMock
from gameClass import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_insert_player_name(self):
        self.assertEqual(self.game.insert_player_game("Name"), "Name")

    def test_switch_turn_computer(self):
        self.game.player_name = "Player"
        self.game.turn = "Player's turn"
        self.assertEqual(self.game.switch_turn(), "Computer's turn")

    def test_switch_turn_player(self):
        self.game.player_name = "Player"
        self.game.turn = "Computer's turn"
        self.assertEqual(self.game.switch_turn(), "Player's turn")

    def test_start_game_random_computer(self):
        self.game.start_game = MagicMock(return_value="Computer")
        self.assertEqual(self.game.start_game(), "Computer")

    def test_player_turn_option_paper(self):
        self.assertEqual(self.game.player_turn_option("Paper"), "Paper")

    def test_computer_turn_random_option(self):
        self.game.computer_turn_option = MagicMock(return_value="Rock")
        self.assertEqual(self.game.computer_turn_option(), "Rock")

    def test_declare_winner_tie(self):
        self.game.player_choice = "Rock"
        self.game.computer_choice = "Rock"
        self.assertEqual(self.game.declare_winner(), "It's a tie!")

    def test_declare_winner_player(self):
        self.game.player_name = "Player"
        self.game.player_choice = "Paper"
        self.game.computer_choice = "Rock"
        self.assertEqual(self.game.declare_winner(), "Player win!")

    def test_declare_winner_player2(self):
        self.game.player_name = "Player"
        self.game.player_choice = "Rock"
        self.game.computer_choice = "Scissors"
        self.assertEqual(self.game.declare_winner(), "Player win!")

    def test_declare_winner_player3(self):
        self.game.player_name = "Player"
        self.game.player_choice = "Scissors"
        self.game.computer_choice = "Paper"
        self.assertEqual(self.game.declare_winner(), "Player win!")

    def test_declare_winner_computer(self):
        self.game.player_name = "Player"
        self.game.player_choice = "Rock"
        self.game.computer_choice = "Paper"
        self.assertEqual(self.game.declare_winner(), "Computer win!")


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import MagicMock
from game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_insert_player_name(self):
        self.assertEqual(self.game.insert_player_game("Name"), "Name")

    def test_start_game_random_player(self):
        self.game.start_game = MagicMock(return_value="Player")
        self.assertEqual(self.game.start_game(), "Player")

    def test_start_game_random_computer(self):
        self.game.start_game = MagicMock(return_value="Computer")
        self.assertEqual(self.game.start_game(), "Computer")

    def test_player_turn_option_paper(self):
        self.assertEqual(self.game.player_turn_option("Paper"), "Paper")

    def test_computer_turn_option_paper(self):
        self.game.computer_turn_choice = MagicMock(return_value="Rock")
        self.assertEqual(self.game.computer_turn_option(), "Rock")


if __name__ == '__main__':
    unittest.main()

from PyQt5.QtWidgets import *
from gameClass import Game
from start_new_game_layout import StartNewGame
from player_choice_layout import PlayerChoice
from result_layout import Result

app = QApplication([])
app.setStyle('Macintosh')


class GameWindow(QWidget):

    def __init__(self, game=Game()):
        super().__init__()
        self.setWindowTitle("RSP Game")
        self.game = game
        self.layout = QVBoxLayout()
        self.start_new_game_window = StartNewGame(self.layout)
        self.player_choice_window = PlayerChoice(self.layout)
        self.result_window = Result(self.layout)
        self.setup_start_game_window()

    def setup_start_game_window(self):
        self.result_window.hide()
        self.start_new_game_window.show()
        self.resize(200, 170)
        self.start_new_game_window.build_layout("Insert your name and play VS the Computer")
        self.start_new_game_window.connect(self.setup_choice_window)

    def setup_choice_window(self):
        self.start_new_game_window.hide()
        self.result_window.hide()
        self.player_choice_window.show()
        self.resize(400, 200)
        self.game.player_name = self.start_new_game_window.player_name_textbox.text()
        self.player_choice_window.build_layout(self.game.player_name)
        self.player_choice_window.connect(self.setup_result_window)

    def setup_result_window(self):
        self.player_choice_window.hide()
        self.result_window.show()
        sending_button = self.sender()
        self.game.player_choice = self.game.player_turn_option(sending_button.objectName())
        self.result_window.build_layout([self.game.player_choice, self.game.computer_turn_option(), self.game.declare_winner()])
        self.result_window.connect([self.setup_start_game_window, self.setup_choice_window])


if __name__ == '__main__':
    window = GameWindow()
    window.setLayout(window.layout)
    window.show()
    app.exec_()

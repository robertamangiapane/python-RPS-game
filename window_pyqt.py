from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
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
        # self.player_name_label = QLabel()
        # self.player_name_textbox = QLineEdit(self)
        # self.computer_choice = QLabel()
        # self.game_result = QLabel()
        # self.new_game_button = QPushButton()
        # self.new_match_button = QPushButton()
        # self.paper_button = QPushButton()
        # self.rock_button = QPushButton()
        # self.scissors_button = QPushButton()
        self.setup_start_game_window()

    def setup_start_game_window(self):
        self.resize(200, 170)
        self.start_new_game_window.build_layout("Insert your name and play VS the Computer")
        # self.player_name_label.setText("<font color=white size=5>Insert your name and play VS the Computer</font>")
        # self.player_name_label.setAlignment(Qt.AlignTop)
        # self.layout.addWidget(self.player_name_label)

        # self.player_name_textbox.move(30, 70)
        # self.player_name_textbox.resize(350, 35)
        # self.player_name_textbox.setAlignment(Qt.AlignCenter)
        # font = self.player_name_textbox.font()
        # font.setPointSize(23)
        # self.player_name_textbox.setFont(font)

        # self.new_game_button.setText('Start Game')
        # self.new_match_button.setText('New Match')

        self.start_new_game_window.connect(self.setup_choice_window)

        # self.start_new_game.new_game_button.clicked.connect(self.setup_choice_window)
        # self.layout.addWidget(self.new_game_button)

    def setup_choice_window(self):
        self.start_new_game_window.hide()
        self.resize(400, 200)
        self.game.player_name = self.start_new_game_window.player_name_textbox.text()
        self.player_choice_window.build_layout(self.game.player_name)

        #     # get_name function to assign the name
        # self.start_new_game.player_name_label.setText("<font color=white size=10>Hello {}, "
        #                                "choose one option:</font>".format(
        #     self.start_new_game.player_name_textbox.text()))

        #
        #     self.player_name_textbox.hide()
        #     self.new_game_button.hide()
        #     self.rock_button.setText('Rock')
        #     self.paper_button.setText('Paper')
        #     self.scissors_button.setText('Scissors')
        #
        #     self.rock_button.setObjectName('Rock')
        #     self.paper_button.setObjectName('Paper')
        #     self.scissors_button.setObjectName('Scissors')
        #
        #     self.layout.addWidget(self.rock_button)
        #     self.layout.addWidget(self.paper_button)
        #     self.layout.addWidget(self.scissors_button)
        #
        # self.rock_button.clicked.connect(self.setup_result_window)
        # self.paper_button.clicked.connect(self.setup_result_window)
        # self.scissors_button.clicked.connect(self.setup_result_window)

        self.player_choice_window.connect(self.setup_result_window)


    def setup_result_window(self):
        self.player_choice_window.hide()
        sending_button = self.sender()
        self.game.player_choice = self.game.player_turn_option(sending_button.objectName())
        self.result_window.build_layout([self.game.player_choice, self.game.computer_turn_option(), self.game.declare_winner()])
        self.result_window.connect([self.setup_start_game_window, self.setup_choice_window])
    #     self.player_name_label.setText("<font color=white size=10>You chose: {}</font>".format(self.game.player_choice))
    #     self.computer_choice.setText("<font color=white size=10>Computer chose: {}</font>".format(self.game.computer_turn_option()))
    #     self.game_result.setText("<font color=red size=10>Game Result: {}</font>".format(self.game.declare_winner()))
    #
    #     self.layout.addWidget(self.computer_choice)
    #     self.layout.addWidget(self.game_result)
    #
    #     self.rock_button.hide()
    #     self.paper_button.hide()
    #     self.scissors_button.hide()
    #
    #     self.layout.addWidget(self.new_game_button, alignment=Qt.AlignBottom)
    #     self.layout.addWidget(self.new_match_button, alignment=Qt.AlignBottom)
    #     self.new_game_button.show()
    #     self.new_match_button.show()
    #     self.new_game_button.clicked.connect(self.setup_main_window)
    #     self.new_match_button.clicked.connect(self.new_game_window)


if __name__ == '__main__':
    window = GameWindow()
    window.setLayout(window.layout)
    window.show()
    app.exec_()

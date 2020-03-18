from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from gameClass import Game

app = QApplication([])
app.setStyle('Macintosh')


class GameWindow(QWidget):

    def __init__(self, game=Game()):
        super().__init__()
        self.setWindowTitle("RSP Game")
        self.game = game
        self.layout = QVBoxLayout()
        self.player_label = QLabel()
        self.player_name_textbox = QLineEdit(self)
        self.computer_choice = QLabel()
        self.game_result = QLabel()
        self.start_game_button = QPushButton()
        self.paper_button = QPushButton()
        self.rock_button = QPushButton()
        self.scissors_button = QPushButton()

        self.setup_main_window()

    def setup_main_window(self):
        self.resize(200, 170)

        self.player_label.setText("<font color=white size=5>Insert your name and play VS the Computer</font>")
        self.player_label.setAlignment(Qt.AlignTop)
        self.layout.addWidget(self.player_label)

        self.player_name_textbox.move(30, 70)
        self.player_name_textbox.resize(350, 35)
        self.player_name_textbox.setAlignment(Qt.AlignCenter)
        font = self.player_name_textbox.font()
        font.setPointSize(23)
        self.player_name_textbox.setFont(font)

        self.start_game_button.setText('Start New Game')
        self.start_game_button.clicked.connect(self.setup_game_window)
        self.layout.addWidget(self.start_game_button)

    def setup_game_window(self):
        self.resize(400, 200)
        self.game.player_name = self.player_name_textbox.text()
        self.player_label.setText("<font color=white size=10>Hello {}, "
                                  "choose one option:</font>".format(self.player_name_textbox.text()))

        self.player_name_textbox.hide()
        self.start_game_button.hide()
        self.rock_button.setText('Rock')
        self.paper_button.setText('Paper')
        self.scissors_button.setText('Scissors')

        self.rock_button.setObjectName('Rock')
        self.paper_button.setObjectName('Paper')
        self.scissors_button.setObjectName('Scissors')

        self.layout.addWidget(self.rock_button)
        self.layout.addWidget(self.paper_button)
        self.layout.addWidget(self.scissors_button)

        self.rock_button.clicked.connect(self.on_choice_clicked)
        self.paper_button.clicked.connect(self.on_choice_clicked)
        self.scissors_button.clicked.connect(self.on_choice_clicked)

    def on_choice_clicked(self):
        sending_button = self.sender()
        self.game.player_choice = self.game.player_turn_option(sending_button.objectName())
        self.player_label.setText("<font color=white size=10>You chose: {}</font>".format(self.game.player_choice))
        self.computer_choice.setText("<font color=white size=10>Computer chose: {}</font>".format(self.game.computer_turn_option()))
        self.game_result.setText("<font color=red size=10>Game Result: {}</font>".format(self.game.declare_winner()))

        self.layout.addWidget(self.computer_choice)
        self.layout.addWidget(self.game_result)

        self.rock_button.hide()
        self.paper_button.hide()
        self.scissors_button.hide()

        self.layout.addWidget(self.start_game_button, alignment=Qt.AlignBottom)
        self.start_game_button.show()
        self.start_game_button.clicked.connect(self.setup_game_window)


if __name__ == '__main__':
    window = GameWindow()
    window.setLayout(window.layout)
    window.show()
    app.exec_()

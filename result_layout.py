from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from main_layout import MainLayout


class Result(MainLayout):

    def __init__(self, layout):
        super().__init__(layout)
        self.player_name_label = QLabel()
        self.computer_choice = QLabel()
        self.game_result = QLabel()
        self.new_game_button = QPushButton()
        self.new_match_button = QPushButton()

    def build_layout(self, arguments):
        super().build_layout(arguments)
        self.layout.addWidget(self.player_name_label)
        self.layout.addWidget(self.computer_choice)
        self.layout.addWidget(self.game_result)
        self.new_game_button.setText('Start Game')
        self.new_match_button.setText('New Match')

        self.player_name_label.setText("<font color=white size=10>You chose: {}</font>".format(arguments[0]))
        self.computer_choice.setText("<font color=white size=10>Computer chose: {}</font>".format(arguments[1]))
        self.game_result.setText("<font color=red size=10>Game Result: {}</font>".format(arguments[2]))

    def connect(self, connection):
        self.new_game_button.clicked.connect(connection[0])
        self.new_match_button.clicked.connect(connection[1])

    def show(self):
        super().show()

    def hide(self):
        super().hide()
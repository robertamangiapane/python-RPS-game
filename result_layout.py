from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from main_layout import MainLayout


class Result(MainLayout):

    def __init__(self, layout):
        super().__init__(layout)
        self.player_name_label = QLabel()
        self.computer_choice = QLabel()
        self.game_result = QLabel()
        self.new_match_button = QPushButton()
        self.new_game_button = QPushButton()

    def build_layout(self, arguments):
        super().build_layout(arguments)
        self.layout.addWidget(self.player_name_label)
        self.layout.addWidget(self.computer_choice)
        self.layout.addWidget(self.game_result)

        self.new_game_button.setText('Start New Game')
        self.new_match_button.setText('Play again')
        self.layout.addWidget(self.new_match_button, alignment=Qt.AlignBottom)
        self.layout.addWidget(self.new_game_button, alignment=Qt.AlignBottom)

        self.player_name_label.setText("<font color=white size=10>You chose: {}</font>".format(arguments[0]))
        self.computer_choice.setText("<font color=white size=10>Computer chose: {}</font>".format(arguments[1]))
        self.game_result.setText("<font color=red size=10>Game Result: {}</font>".format(arguments[2]))

    def connect(self, connection):
        self.new_game_button.clicked.connect(connection[0])
        self.new_match_button.clicked.connect(connection[1])

    def show(self):
        self.player_name_label.show()
        self.computer_choice.show()
        self.game_result.show()
        self.new_game_button.show()
        self.new_match_button.show()

    def hide(self):
        self.player_name_label.hide()
        self.computer_choice.hide()
        self.game_result.hide()
        self.new_game_button.hide()
        self.new_match_button.hide()

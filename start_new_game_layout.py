from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from main_layout import MainLayout


class StartNewGame(MainLayout):

    def __init__(self, layout):
        super().__init__(layout)
        self.new_game_button = QPushButton()
        self.player_name_label = QLabel()
        self.player_name_textbox = QLineEdit()

    def build_layout(self, text):
        super().build_layout(text)
        self.layout.addWidget(self.player_name_label)
        self.player_name_label.setText("<font color=white size=5>{}</font>".format(text))
        self.player_name_label.setAlignment(Qt.AlignTop)

        self.player_name_textbox.clear()
        self.player_name_textbox.move(30, 70)
        self.player_name_textbox.resize(350, 35)
        self.player_name_textbox.setAlignment(Qt.AlignCenter)
        font = self.player_name_textbox.font()
        font.setPointSize(23)
        self.player_name_textbox.setFont(font)
        self.layout.addWidget(self.player_name_textbox)

        self.new_game_button.setText('Start Game')
        self.layout.addWidget(self.new_game_button, alignment=Qt.AlignBottom)

    def connect(self, connection):
        self.new_game_button.clicked.connect(connection)

    def show(self):
        self.player_name_label.show()
        self.player_name_textbox.show()
        self.new_game_button.show()

    def hide(self):
        self.player_name_label.hide()
        self.player_name_textbox.hide()
        self.new_game_button.hide()




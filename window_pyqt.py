from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from gameClass import Game

app = QApplication([])
app.setStyle('Macintosh')


class GameWindow(QWidget):

    def __init__(self, window_title, height, width, player_name):
        super().__init__()
        self.window_title = window_title
        self.height = height
        self.width = width
        self.player_name = player_name
        self.layout = QVBoxLayout()
        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.window_title)
        self.resize(self.height, self.width)

        label_player = QLabel("<font color=white size=10>{}</font>".format(self.player_name))
        label_player.setAlignment(Qt.AlignTop)

        rock_button = QPushButton('Rock')
        paper_button = QPushButton('Paper')
        scissors_button = QPushButton('Scissors')

        label_computer = QLabel("<font color=white size=10>Computer choice</font>")
        label_game_result = QLabel("<font color=red size=10>Game Result</font>")

        self.layout.addWidget(label_player)
        self.layout.addWidget(rock_button)
        self.layout.addWidget(paper_button)
        self.layout.addWidget(scissors_button)
        self.layout.addWidget(label_computer)
        self.layout.addWidget(label_game_result)


if __name__ == '__main__':
    window = GameWindow("RSP Game", 1000, 700, "Roberta")
    window.setLayout(window.layout)
    window.show()
    app.exec_()

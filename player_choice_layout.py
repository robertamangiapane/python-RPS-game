from PyQt5.QtWidgets import *
from main_layout import MainLayout


class PlayerChoice(MainLayout):

    def __init__(self, layout):
        super().__init__(layout)
        self.player_name_label = QLabel()
        self.paper_button = QPushButton()
        self.rock_button = QPushButton()
        self.scissors_button = QPushButton()

    def build_layout(self, player_name):
        super().build_layout(player_name)
        self.layout.addWidget(self.player_name_label)
        self.player_name_label.setText("<font color=white size=10>Hello {}, "
                                       "choose one option:</font>".format(player_name))
        self.rock_button.setText('Rock')
        self.paper_button.setText('Paper')
        self.scissors_button.setText('Scissors')
        self.rock_button.setObjectName('Rock')
        self.paper_button.setObjectName('Paper')
        self.scissors_button.setObjectName('Scissors')
        self.layout.addWidget(self.rock_button)
        self.layout.addWidget(self.paper_button)
        self.layout.addWidget(self.scissors_button)

    def connect(self, connection):
        self.rock_button.clicked.connect(connection)
        self.paper_button.clicked.connect(connection)
        self.scissors_button.clicked.connect(connection)

    def show(self):
        self.player_name_label.show()
        self.rock_button.show()
        self.paper_button.show()
        self.scissors_button.show()

    def hide(self):
        self.player_name_label.hide()
        self.rock_button.hide()
        self.paper_button.hide()
        self.scissors_button.hide()

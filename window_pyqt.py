from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

app = QApplication([])
app.setStyle('Macintosh')

window = QWidget()
window.setWindowTitle('RPS Game')
window.resize(1000, 700)
layout = QVBoxLayout()

label_Player = QLabel("<font color=white size=10>Player's name</font>")
label_Player.setAlignment(Qt.AlignTop)

rock_button = QPushButton('Rock')
paper_button = QPushButton('Paper')
scissors_button = QPushButton('Scissors')

label_Computer = QLabel("<font color=white size=10>Computer choice</font>")
label_Game_Result = QLabel("<font color=red size=10>Game Result</font>")

layout.addWidget(label_Player)
layout.addWidget(rock_button)
layout.addWidget(paper_button)
layout.addWidget(scissors_button)
layout.addWidget(label_Computer)
layout.addWidget(label_Game_Result)

window.setLayout(layout)
window.show()
app.exec_()

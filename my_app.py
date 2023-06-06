from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, 
                             QLabel, QPushButton, 
                             QVBoxLayout, QHBoxLayout)
from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        self.button_next = QPushButton(txt_next)
        self.welcome_txt = QLabel(txt_hello)
        self.instr_txt = QLabel(txt_instruction)
        self.line = QVBoxLayout()

        self.line.addWidget(self.welcome_txt, alignment = Qt.AlignCenter)
        self.line.addWidget(self.instr_txt, alignment = Qt.AlignCenter)
        self.line.addWidget(self.button_next, alignment = Qt.AlignCenter)
        self.setLayout(self.line)

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.button_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])
mw = MainWin()
app.exec_()
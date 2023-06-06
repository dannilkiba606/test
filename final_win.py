from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, 
                             QLabel, QVBoxLayout, QHBoxLayout)
from instr import *


class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.show()

    def initUI(self):
        self.wh_txt = QLabel(txt_workheart)
        self.index_txt = QLabel(txt_index)

        self.line1 = QVBoxLayout()

        self.line1.addWidget(self.wh_txt, alignment = Qt.AlignCenter)
        self.line1.addWidget(self.index_txt, alignment = Qt.AlignCenter)

        self.setLayout(self.line1)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

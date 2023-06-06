from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QApplication, 
                             QLabel, QPushButton, 
                             QLineEdit, QHBoxLayout, QHBoxLayout)
from instr import *
from final_win import *

class TestWin(QWidget):
    '''Класс второго окна с тестами и с теми же методами, что имеет начальное ознакомительное окно'''
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        # создаем виджеты кнопок
        self.button_next = QPushButton(txt_sendresults)
        self.button_test1 = QPushButton(txt_starttest1)
        self.button_test2 = QPushButton(txt_starttest2)
        self.button_test3 = QPushButton(txt_starttest3)

        # создаем виджеты текста
        self.name_txt = QLabel(txt_name)
        self.age_txt = QLabel(txt_age)
        self.test1_txt = QLabel(txt_test1)
        self.test2_txt = QLabel(txt_test2)
        self.test3_txt = QLabel(txt_test3)
        self.timer_txt = QLabel(txt_timer)

        # создаем виджеты полей ввода
        self.l_name = QLineEdit(txt_hintname)
        self.l_age = QLineEdit(txt_hintage)
        self.l_test1 = QLineEdit(txt_hinttest1)
        self.l_test2 = QLineEdit(txt_hinttest2)
        self.l_test3 = QLineEdit(txt_hinttest3)

        # создаем направляющие линии
        self.r_line = QVBoxLayout() # правая вертикальная
        self.l_line = QVBoxLayout() # левая вертикальная
        self.h_line = QHBoxLayout() # основная центральная горизонтальная

        self.r_line.addWidget(self.timer_txt, alignment = Qt.AlignCenter) # таймер будет справа, а все остальное слева
        self.l_line.addWidget(self.name_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.l_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.age_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.l_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.l_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test1_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.l_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test2_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.l_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test3_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_next, alignment = Qt.AlignLeft)

        # обьединяем линии
        self.h_line.addLayout(self.r_line)
        self.h_line.addLayout(self.l_line)

        self.setLayout(self.h_line)

    # функция для нажатия кнопки для перехода в следующее окно
    def next_click(self):
        self.hide()
        self.fw = FinalWin()

    # "коннектим" кнопку и метод next_click
    def connects(self):
        self.button_next.clicked.connect(self.next_click)

    # настраиваем окно(название, размер, координаты появления)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


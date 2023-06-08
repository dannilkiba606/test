from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QApplication, 
                             QLabel, QPushButton, 
                             QLineEdit, QHBoxLayout, QHBoxLayout)
from instr import *
from final_win import *

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3

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
        self.l_line = QVBoxLayout() # правая вертикальная
        self.r_line = QVBoxLayout() # левая вертикальная
        self.h_line = QHBoxLayout() # основная центральная горизонтальная

        self.r_line.addWidget(self.timer_txt, alignment = Qt.AlignCenter) # таймер будет справа, а все остальное слева
        self.l_line.addWidget(self.name_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.l_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.age_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.l_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test1_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.l_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test2_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.test3_txt, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.l_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.l_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_next, alignment = Qt.AlignLeft)

        # обьединяем линии
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)

        self.setLayout(self.h_line)

    # функция для нажатия кнопки для перехода в следующее окно
    def next_click(self):
        self.hide()
        self.exp = Experiment(int(self.l_age.text()), self.l_test1.text(), self.l_test2.text(), self.l_test3.text())
        self.fw = FinalWin(self.exp)

    # "коннектим" кнопку и метод next_click
    def connects(self):
        self.button_next.clicked.connect(self.next_click)
        self.button_test1.clicked.connect(self.timer_test)
        self.button_test2.clicked.connect(self.timer_sits)
        self.button_test3.clicked.connect(self.timer_final)

    # настраиваем окно(название, размер, координаты появления)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_txt.setText(time.toString("hh:mm:ss"))
        self.timer_txt.setStyleSheet("color: rgb(0,0,0)")
        self.timer_txt.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_txt.setText(time.toString("hh:mm:ss")[6:])
        self.timer_txt.setStyleSheet("color: rgb(0, 0, 0)")
        self.timer_txt.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss")[6:] == "00":
            self.timer.stop()

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.timer_txt.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:]) >= 45:
            self.timer_txt.setStyleSheet("color: rgb(0, 255, 0)")
        elif int(time.toString("hh:mm:ss")[6:]) <= 15:
            self.timer_txt.setStyleSheet("color: rgb(0, 255, 0)")
        else:
            self.timer_txt.setStyleSheet("color: rgb(0, 0, 0)")
        self.timer_txt.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()



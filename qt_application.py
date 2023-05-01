import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QRadioButton, QHBoxLayout, \
                            QVBoxLayout, QLayout, QSizePolicy
from PyQt5.QtGui import QFont


class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.status = '@'
        self.setGeometry(0, 0, 300, 300)
        self.setWindowTitle('Собаки и кошки')

        # Объявление вспомогательных переменных
        max_size = QSizePolicy()
        max_size.setVerticalPolicy(7)
        max_size.setHorizontalPolicy(7)
        font1 = QFont()
        font1.setFamily("Futura")
        font1.setPointSize(40)
        font2 = QFont()
        font2.setFamily("Futura")
        font2.setPointSize(17)

        # Объявление списков
        self.buttons = []
        self.rows = []

        # Осноной лэйаут
        self.main_layout = QVBoxLayout(self)

        # Лэйаут с двумя верхними кнопками
        self.change_fm = QHBoxLayout()
        self.change_fm.setSizeConstraint(QLayout.SizeConstraint(2))
        self.main_layout.addLayout(self.change_fm)

        # Лэйаут игрового поля
        self.game_field_layout = QVBoxLayout(self)
        self.game_field_layout.setSizeConstraint(QLayout.SizeConstraint(4))
        self.main_layout.addLayout(self.game_field_layout)

        # Создание лэйаутов для рядо кнопок
        for _ in range(3):
            a = QHBoxLayout()
            a.setSizeConstraint(QLayout.SetDefaultConstraint)
            a.setSpacing(15)
            self.rows.append(a)
            self.game_field_layout.addLayout(a)

        # Создание и занесение в лэйаут кнопок
        for i in range(3):
            for j in range(3):
                btn = QPushButton(self)
                btn.setMinimumSize(150, 150)
                btn.setSizePolicy(max_size)
                btn.setFont(font1)
                btn.clicked.connect(self.turn)
                self.buttons.append(btn)
                self.rows[i].addWidget(btn)

        # Надпись о победившем игроке
        self.message = QLabel(self)
        self.message.setFont(font2)
        self.message.close()
        self.main_layout.addWidget(self.message)

        # Следующии две кнопки являются трекерами очерёдности хода
        # Нажав на одну из них можно выбрать кто ходит первым

        # Левая верхняя кнопка
        self.X = QRadioButton(self)
        self.X.setText('@')
        self.X.setFont(font2)
        self.X.clicked.connect(self.new_game_RB)
        self.X.click()
        self.change_fm.addWidget(self.X)

        # Правая верхняя кнопка
        self.O = QRadioButton(self)
        self.O.setText('^_^')
        self.O.setFont(font2)
        self.O.clicked.connect(self.new_game_RB)
        self.change_fm.addWidget(self.O)

        # Самая нижняя кнопка
        self.ng = QPushButton('Start new game', self)
        self.sizeHint()
        self.setFont(font2)
        self.ng.clicked.connect(self.new_game_PB)
        self.main_layout.addWidget(self.ng)

    def turn(self):
        if self.status == '@':
            self.sender().setText('@')
            self.status = '^_^'
            self.X.setChecked(False)
            self.O.setChecked(True)
        else:
            self.sender().setText('^_^')
            self.status = '@'
            self.O.setChecked(False)
            self.X.setChecked(True)

        self.sender().setDisabled(True)

        game_over = [self.buttons[4].text() == self.buttons[2].text() == self.buttons[6].text() != '',
                     self.buttons[0].text() == self.buttons[4].text() == self.buttons[8].text() != '',
                     self.buttons[0].text() == self.buttons[3].text() == self.buttons[6].text() != '',
                     self.buttons[1].text() == self.buttons[4].text() == self.buttons[7].text() != '',
                     self.buttons[2].text() == self.buttons[5].text() == self.buttons[8].text() != '',
                     self.buttons[0].text() == self.buttons[1].text() == self.buttons[2].text() != '',
                     self.buttons[3].text() == self.buttons[4].text() == self.buttons[5].text() != '',
                     self.buttons[6].text() == self.buttons[7].text() == self.buttons[8].text() != '']

        for over in game_over:
            if over:
                for button in self.buttons:
                    button.setDisabled(True)
                if self.sender().text() == '@':
                    self.message.setText('Dog wins')
                else:
                    self.message.setText('Cat wins')
                self.message.show()
                break

            if len(list(filter(lambda z: len(z.text()) != 0, self.buttons))) == 9:
                for button in self.buttons:
                    button.setDisabled(True)
                self.message.setText('Friendship wins')
                self.message.show()

    # Начало игры при нажатии на одну из верхних кнопок
    def new_game_RB(self):
        if self.sender().text() == '@':
            self.status = '@'
        else:
            self.status = '^_^'

        for button in self.buttons:
            button.setText('')
            button.setDisabled(False)
        self.message.close()

    # Начало игры принажатии на верхнюю кнопку
    def new_game_PB(self):
        if self.X.isChecked():
            self.status = '@'
        else:
            self.status = '^_^'

        for button in self.buttons:
            button.setText('')
            button.setDisabled(False)
        self.message.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Game()
    win.show()
    sys.exit(app.exec())

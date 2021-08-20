import sys
import traceback
import logging
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QGridLayout, QLayout)
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def getResult(self):
        formula = self.display.text()
        try:
            result = eval(formula)
        except SyntaxError:
            result = '잘못된 식입니다.'
        except Exception:
            result = '다시 입력해주세요.'
            logging.error(traceback.format_exc())

        self.display.setText(str(result))

    def getBtn(self, number):
        numberBtn = QPushButton(str(number))
        numberBtn.clicked.connect(lambda: self.display.setText(self.display.text() + str(number)))
        return numberBtn

    def setButtons(self):
        clearBtn = QPushButton('Clear')
        clearBtn.clicked.connect(lambda: self.display.setText(''))

        delBtn = QPushButton('Del')
        delBtn.clicked.connect(lambda: self.display.setText(self.display.text()[:-1]))

        resultBtn = QPushButton('=')
        resultBtn.clicked.connect(self.getResult)

        self.gridLayout.addWidget(self.display, 0, 0, 1, 4)
        self.gridLayout.addWidget(clearBtn, 1, 0, 1, 2)
        self.gridLayout.addWidget(delBtn, 1, 2, 1, 2)
        self.gridLayout.addWidget(self.getBtn('1'), 2, 0)
        self.gridLayout.addWidget(self.getBtn('2'), 2, 1)
        self.gridLayout.addWidget(self.getBtn('3'), 2, 2)
        self.gridLayout.addWidget(self.getBtn('+'), 2, 3)
        self.gridLayout.addWidget(self.getBtn('4'), 3, 0)
        self.gridLayout.addWidget(self.getBtn('5'), 3, 1)
        self.gridLayout.addWidget(self.getBtn('6'), 3, 2)
        self.gridLayout.addWidget(self.getBtn('-'), 3, 3)
        self.gridLayout.addWidget(self.getBtn('7'), 4, 0)
        self.gridLayout.addWidget(self.getBtn('8'), 4, 1)
        self.gridLayout.addWidget(self.getBtn('9'), 4, 2)
        self.gridLayout.addWidget(self.getBtn('*'), 4, 3)
        self.gridLayout.addWidget(self.getBtn('0'), 5, 0)
        self.gridLayout.addWidget(self.getBtn('.'), 5, 1)
        self.gridLayout.addWidget(resultBtn, 5, 2)
        self.gridLayout.addWidget(self.getBtn('/'), 5, 3)

    def initUI(self):
        self.display = QLineEdit()  # Line editor 생성
        self.display.setReadOnly(True)  # 입력이 되지 않도록
        self.display.setAlignment(Qt.AlignRight)  # 우측으로 정렬
        self.display.setStyleSheet(
            "border:0px; font-size:20pt; font-family:Nanum Gothic; font-weight:bold; padding:10px"
        )

        self.gridLayout = QGridLayout()
        self.setLayout(self.gridLayout)
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)

        self.setButtons()

        self.setWindowTitle('My Calculator')
        self.setFixedSize(300, 400)  # 고정된 크기 설정
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

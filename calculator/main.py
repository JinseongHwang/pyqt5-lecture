import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout,
                             QToolButton, QSizePolicy, QLineEdit, QGridLayout, QLayout)
from PyQt5.QtCore import Qt, QCoreApplication


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.display = QLineEdit("0")  # 기본으로 0이 표시되게.
        self.display.setReadOnly(True)  # 입력이 되지 않도록
        self.display.setAlignment(Qt.AlignRight)  # 우측으로 정렬
        self.display.setStyleSheet(
            "border:0px; font-size:20pt; font-family:Nanum Gothic; font-weight:bold; padding:10px"
        )

        gridLayout = QGridLayout()
        self.setLayout(gridLayout)
        gridLayout.setSizeConstraint(QLayout.SetFixedSize)

        gridLayout.addWidget(self.display, 0, 0, 1, 4)
        gridLayout.addWidget(QPushButton('Clear'), 1, 0, 1, 2)
        gridLayout.addWidget(QPushButton('Del'), 1, 2, 1, 2)
        gridLayout.addWidget(QPushButton('1'), 2, 0)
        gridLayout.addWidget(QPushButton('2'), 2, 1)
        gridLayout.addWidget(QPushButton('3'), 2, 2)
        gridLayout.addWidget(QPushButton('+'), 2, 3)
        gridLayout.addWidget(QPushButton('4'), 3, 0)
        gridLayout.addWidget(QPushButton('5'), 3, 1)
        gridLayout.addWidget(QPushButton('6'), 3, 2)
        gridLayout.addWidget(QPushButton('-'), 3, 3)
        gridLayout.addWidget(QPushButton('7'), 4, 0)
        gridLayout.addWidget(QPushButton('8'), 4, 1)
        gridLayout.addWidget(QPushButton('9'), 4, 2)
        gridLayout.addWidget(QPushButton('*'), 4, 3)
        gridLayout.addWidget(QPushButton('0'), 5, 0)
        gridLayout.addWidget(QPushButton('.'), 5, 1)
        gridLayout.addWidget(QPushButton('='), 5, 2)
        gridLayout.addWidget(QPushButton('/'), 5, 3)

        self.setWindowTitle('My Calculator')
        self.setFixedSize(300, 400)  # 고정된 크기 설정
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

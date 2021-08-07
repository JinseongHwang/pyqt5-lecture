import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QComboBox
)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        comboBox = QComboBox()
        comboBox.addItems(['1', '2', '3', '4', '5'])

        #####
        # addWidget(Object, Row, Column)
        #####
        grid.addWidget(QLabel('Title:'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Rate:'), 2, 0)
        grid.addWidget(QLabel('Review:'), 3, 0)

        grid.addWidget(QLineEdit(), 0, 1)  # Line editor
        grid.addWidget(QLineEdit(), 1, 1)  # Line editor
        grid.addWidget(comboBox, 2, 1)
        grid.addWidget(QTextEdit(), 3, 1)  # Text editor

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

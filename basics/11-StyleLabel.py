import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        labelRed = QLabel('Red')
        labelGreen = QLabel('Green')
        labelBlue = QLabel('Blue')

        labelRed.setStyleSheet("color: red;"
                              "border-style: solid;"
                              "border-width: 2px;"
                              "border-color: #FA8072;"
                              "border-radius: 5px")
        labelGreen.setStyleSheet("color: green;"
                                "background-color: #7FFFD4")
        labelBlue.setStyleSheet("color: blue;"
                               "background-color: #87CEFA;"
                               "border-style: dashed;"
                               "border-width: 3px;"
                               "border-color: #1E90FF")

        vbox = QVBoxLayout()
        vbox.addWidget(labelRed)
        vbox.addWidget(labelGreen)
        vbox.addWidget(labelBlue)

        self.setLayout(vbox)

        self.setWindowTitle('Stylesheet')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

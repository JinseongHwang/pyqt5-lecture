import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.closeBtn()
        self.initUI()

    def closeBtn(self):
        # QPushButton(Text, 버튼이 위치할 부모 위젯)
        btn = QPushButton('Quit', self)
        btn.setGeometry(100, 100, 100, 100)
        # clicked 이벤트가 발생하면 현재 instance()를 quit 한다.
        btn.clicked.connect(QCoreApplication.instance().quit)

    def initUI(self):
        self.setWindowTitle('Quit Button')
        self.setGeometry(300, 400, 400, 500)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.setWindowIcon(QIcon(
            'C:\\Users\\User\\Desktop\\my-lecture-material\\pyqt5-lecture\\resources\\icon.png'))
        # 위치 (x, y), 창 크기 (width, height)
        self.setGeometry(400, 400, 700, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

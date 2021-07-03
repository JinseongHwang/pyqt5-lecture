import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('Label1', self)
        label1.move(20, 20)  # move(X, Y) : 정해준 위치 좌표로 이동(절대적 배치)
        label2 = QLabel('Label2', self)
        label2.move(20, 60)

        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)

        #####
        # 동일한 객체에 대해서 move()를 많이 하면, 마지막에 했던 것 하나만 적용된다.
        #####

        self.setWindowTitle('Absolute Positioning')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

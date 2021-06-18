import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.simpleBtn()
        self.closeBtn()
        self.initUI()

    def simpleBtn(self):
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(50, 50)  # 버튼 위치 설정
        btn.resize(btn.sizeHint())  # 버튼 크기는 적당히

    def closeBtn(self):
        # QPushButton(Text, 버튼이 위치할 부모 위젯)
        btn = QPushButton('Quit', self)
        btn.setToolTip('Quit Button')
        btn.move(150, 50)  # 버튼 위치 설정
        btn.resize(btn.sizeHint())  # 버튼 크기는 적당히
        # clicked 이벤트가 발생하면 현재 instance()를 quit 한다.
        btn.clicked.connect(QCoreApplication.instance().quit)

    def initUI(self):
        # 삐침 없는 폰트로, 10 크기
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        self.setWindowTitle('Tooltips')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

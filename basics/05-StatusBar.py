import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.addBtn()
        self.initUI()

    def go(self):
        message = self.statusBar().currentMessage()
        self.statusBar().showMessage(message + ' Go!!')

    def addBtn(self):
        btn = QPushButton('Button', self)
        btn.move(50, 50)  # 버튼 위치 설정
        btn.resize(btn.sizeHint())  # 버튼 크기는 적당히
        btn.clicked.connect(self.go)  # 클릭 시 발생할 이벤트 정의

    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setWindowTitle('Statusbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 버튼 3개 생성
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        exitButton = QPushButton('Exit')
        exitButton.clicked.connect(QCoreApplication.instance().quit)  # 종료 기능

        # 수평 박스, [좌:우 = 1:1]
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addWidget(exitButton)
        hbox.addStretch(1)

        # 수직 박스, [상:하 = 3:1]
        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        # 수직 박스를 창의 메인 레이아웃으로 설정
        self.setLayout(vbox)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar()  # 빈 statusBar 생성

        # Icon, Text, 위치하는 부모 객체
        exitAction = QAction(QIcon(
            'C:\\Users\\User\\Desktop\\my-lecture-material\\pyqt5-lecture\\resources\\exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')  # 단축키 Ctrl + Q 사용 가능
        exitAction.setStatusTip('Exit application')  # statusBar 에 나타날 텍스트 지정
        # 이 동작을 선택했을 때 생성된 시그널이 quit 메서드에 연결되어 Application 이 종료됨
        exitAction.triggered.connect(qApp.quit)

        menuBar = self.menuBar()  # 메뉴바 생성
        menuBar.setNativeMenuBar(False)  # MacOS 에서도 동작하도록 하는 설정
        # File 이라는 메뉴를 추가 (Alt + F 로 선택 가능)
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAction)  # File 메뉴에 exitAction 을 추가

        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

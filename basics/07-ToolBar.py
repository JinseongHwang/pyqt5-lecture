import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.toolbar = None  # toolbar 를 __init__ 으로 올려달라는 오류 무시
        self.initUI()

    def initUI(self):
        self.statusBar()

        # exitAction 을 생성합니다.
        exitAction = QAction(QIcon(
            'C:\\Users\\User\\Desktop\\my-lecture-material\\pyqt5-lecture\\resources\\exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        saveAction = QAction(QIcon(
            'C:\\Users\\User\\Desktop\\my-lecture-material\\pyqt5-lecture\\resources\\save.png'), 'Save', self)
        saveAction.setStatusTip('Save application')

        editAction = QAction(QIcon(
            'C:\\Users\\User\\Desktop\\my-lecture-material\\pyqt5-lecture\\resources\\edit.png'), 'Edit', self)
        editAction.setStatusTip('Edit application')

        printAction = QAction(QIcon(
            'C:\\Users\\User\\Desktop\\my-lecture-material\\pyqt5-lecture\\resources\\print.png'), 'Print', self)
        printAction.setStatusTip('Print application')

        self.toolbar = self.addToolBar('Exit')  # ToolBar 에 Exit 을 추가한다.
        self.toolbar.addAction(exitAction)  # exitAction 을 추가한다.

        self.toolbar = self.addToolBar('Save')
        self.toolbar.addAction(saveAction)

        self.toolbar = self.addToolBar('Edit')
        self.toolbar.addAction(editAction)

        self.toolbar = self.addToolBar('Print')
        self.toolbar.addAction(printAction)

        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

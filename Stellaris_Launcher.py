from PyQt5 import QtWidgets, QtCore, QtGui
import sys


class AppMainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setMinimumSize(QtCore.QSize(self.width(), self.height()))
        self.setWindowIcon(QtGui.QIcon('img\\ico1.png'))
        self.setWindowTitle('Stellaris Launcher 2.3 by yohko ')
        vbox = QtWidgets.QVBoxLayout(self)
        wdg = QtWidgets.QWidget()
        wdg.setLayout(vbox)
        play_button = QtWidgets.QPushButton('Play')
        play_button.setFlat(True)
        vbox.addWidget(play_button)
        self.setCentralWidget(wdg)


#  на случай если программа запускается из оболочки
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = AppMainWindow()
    main.show()
    sys.exit(app.exec_())


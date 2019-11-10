from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys


class AppMainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # elements

        self.table = QtWidgets.QTableWidget()
        abst = QtWidgets.QAbstractItemView
        self.table.setSelectionMode(abst.SingleSelection)
        self.table.setSelectionBehavior(abst.SelectRows)
        self.table.setDragDropMode(abst.InternalMove)
        self.table.setDragEnabled(True)
        self.table.setColumnCount(4)
        self.table.setRowCount(4)

        play_button = QtWidgets.QPushButton('Play')
        play_button.setFlat(True)

        accept_button = QtWidgets.QPushButton('Accept')
        accept_button.setFlat(True)

        # window proprieties
        self.setMinimumSize(QtCore.QSize(self.width(), self.height()))
        self.setWindowIcon(QtGui.QIcon('img\\ico1.png'))
        self.setWindowTitle('Stellaris Launcher 2.3 by yohko ')

        vbox = QtWidgets.QVBoxLayout(self)
        wdg = QtWidgets.QWidget()

        vbox.addWidget(self.table)
        vbox.addWidget(accept_button)
        vbox.addWidget(play_button)
        wdg.setLayout(vbox)

        self.setCentralWidget(wdg)


#  на случай если программа запускается из оболочки
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = AppMainWindow()
    main.show()
    sys.exit(app.exec_())


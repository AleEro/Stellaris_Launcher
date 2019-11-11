from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys, json
from table_class import Table, TableData


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # elements
        self.table = Table()
        self.table_dt = TableData()

        play_button = QtWidgets.QPushButton('Play')
        play_button.setFlat(True)
        # play_button.clicked.connect()

        load_btn = QtWidgets.QPushButton('Load')
        load_btn.setFlat(True)
        play_button.clicked.connect(self.fill_table)
        settings = QtWidgets.QPushButton('settings')
        settings.setFlat(True)

        # window proprieties
        self.setMinimumSize(QtCore.QSize(self.width(), self.height()))
        self.setWindowIcon(QtGui.QIcon('img\\ico1.png'))
        self.setWindowTitle('Stellaris Launcher 2.4 by yohko')

        vbox = QtWidgets.QVBoxLayout()
        wdg = QtWidgets.QWidget()

        vbox.addWidget(self.table)
        vbox.addWidget(load_btn)
        vbox.addWidget(play_button)
        vbox.addWidget(settings)
        wdg.setLayout(vbox)

        self.setCentralWidget(wdg)
        self.mods_registry = self.load_fd('mods_registry.json')

    def fill_table(self, a='hello'):
        print(a)

    @staticmethod
    def load_fd(name, dir=r'Stellaris Launcher/'):
        print('ss')
        with open(dir+name, 'r', encoding='utf_8') as data:
            b = json.load(data)
            # print(b)
        return b


#  на случай если программа запускается из оболочки
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

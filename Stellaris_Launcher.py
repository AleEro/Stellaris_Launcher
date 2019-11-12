import sys
import json
from PyQt5 import QtWidgets, QtCore, QtGui
from otherClasses import (
    Table, TableData, Mod, Button)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # elements
        self.table = Table()
        self.table_dt = TableData(self)
        self.mod_list = []

        play_button = Button('Play')
        # play_button.clicked.connect()
        load_btn = Button('Load')
        load_btn.clicked.connect(self.table_dt.fill_data)
        settings = Button('settings')
        settings.clicked.connect(self.settg)

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
        self.mod_list = self.get_md()
        self.table_dt.fill_data()

    @staticmethod
    def load_fd(name, dir=r'Stellaris Launcher/'):
        with open(dir + name, 'r', encoding='utf_8') as data:
            b = json.load(data)
            # print(b)
        return b

    def get_md(self):
        mod_list = []
        for mod_hash, mod_data in self.mods_registry.items():
            # print(data)
            mod = Mod(mod_hash, mod_data)
            mod_list.append(mod)
        return mod_list

    def settg(self):
        for i in self.mod_list:
            print(i.mod_data)
            for j in i.mod_data:
                print(i.mod_data[j])


#  на случай если программа запускается из оболочки
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

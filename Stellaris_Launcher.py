import sys
import json
from PyQt5 import QtWidgets, QtCore, QtGui
from otherClasses import (Table, TableData, Mod, Button)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # elements
        self.table = Table()
        self.table_dt = TableData(self)
        self.mod_list = []

        play_button = Button('Play')
        play_button.clicked.connect(self.play_btn)
        # settings = Button('settings')
        # settings.clicked.connect(self.settings)

        # window proprieties
        self.setMinimumSize(QtCore.QSize(self.width(), self.height()))
        self.setWindowIcon(QtGui.QIcon('img\\ico1.png'))
        self.setWindowTitle('Stellaris Launcher 2.4 by yohko')

        vbox = QtWidgets.QVBoxLayout()
        wdg = QtWidgets.QWidget()

        vbox.addWidget(self.table)
        vbox.addWidget(play_button)
        # vbox.addWidget(settings)
        wdg.setLayout(vbox)

        self.setCentralWidget(wdg)
        self.mods_registry = self.load_fd('mods_registry.json')
        self.game_data = self.load_fd('game_data.json')
        self.mod_list = self.get_mod_list()
        self.fill_data()

    @staticmethod
    def load_fd(name, dir_r=r'Stellaris Launcher/'):
        try:
            with open(dir_r + name, 'r', encoding='utf_8') as data:
                b = json.load(data)
                # print(b)
        except FileNotFoundError:
            with open(dir_r + name, 'w', encoding='utf_8') as data:
                b = json.load(data)
        return b

    def get_mod_list(self):
        mod_list = []
        for mod_hash, mod_data in self.mods_registry.items():
            # print(data)
            mod = Mod(mod_hash, mod_data)
            mod_list.append(mod)
        return mod_list

    def fill_data(self):
        for i in self.mod_list:
            c0 = QtGui.QStandardItem(f'{i.gameRegistryId}')
            c1 = QtGui.QStandardItem(f'{i.source}')
            c2 = QtGui.QStandardItem(f'{i.steamId}')
            c3 = QtGui.QStandardItem(f'{i.displayName}')
            c4 = QtGui.QStandardItem(f'{i.tags}')
            c5 = QtGui.QStandardItem(f'{i.requiredVersion}')
            c6 = QtGui.QStandardItem(f'{i.archivePath}')
            c7 = QtGui.QStandardItem(f'{i.status}')
            c8 = QtGui.QStandardItem(f'{i.Mid}')
            c9 = QtGui.QStandardItem(f'{i.timeUpdated}')
            c10 = QtGui.QStandardItem(f'{i.thumbnailUrl}')
            c11 = QtGui.QStandardItem(f'{i.dirPath}')
            c12 = QtGui.QStandardItem(f'{i.thumbnailPath}')
            list1 = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12]
            for e in list1:
                e.setEditable(False)
                e.setDropEnabled(False)
            self.table_dt.appendRow(list1)
        self.table.setModel(self.table_dt)

    def play_btn(self):
        print('hello')


#  на случай если программа запускается из оболочки
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

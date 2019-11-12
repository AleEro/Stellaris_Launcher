from PyQt5 import QtWidgets, QtCore, QtGui


class Mod():
    def __init__(self, mod_hash, mod_data):
        empt = '-'
        self.mod_hash = mod_hash
        self.mod_data = mod_data
        self.gameRegistryId = mod_data['gameRegistryId'] if 'gameRegistryId' in mod_data else empt
        self.source = mod_data['source'] if 'source' in mod_data else empt
        self.steamId = mod_data['steamId'] if 'steamId' in mod_data else empt
        self.displayName = mod_data['displayName'] if 'displayName' in mod_data else empt
        self.tags = mod_data['tags'] if 'tags' in mod_data else empt


#        self.requiredVersion = requiredVersion
#        self.archivePath = archivePath
#        self.status = status
#        self.Mid = Mid
#        self.timeUpdated = timeUpdated
#        self.thumbnailUrl = thumbnailUrl
#        self.dirPath = dirPath
#        self.thumbnailPath = thumbnailPath


class Button(QtWidgets.QPushButton):
    def __init__(self, text='Button', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText(text)
        self.setFlat(True)


class TableData(QtGui.QStandardItemModel):
    def __init__(self, root, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root
        self.setRowCount(6)
        self.setColumnCount(6)

    def fill_data(self):
        pass

    def get_from_data(self):
        pass


class Table(QtWidgets.QTableView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sim = TableData(self)
        self.setModel(self.sim)
        self.setSelectionMode(self.SingleSelection)
        self.setSelectionBehavior(self.SelectRows)
        self.setEditTriggers(self.NoEditTriggers)
        self.setDragDropMode(self.InternalMove)
        self.setDragEnabled(True)
        # self.setGridStyle(QtCore.Qt.NoPen)
        self.setShowGrid(False)

    def on_drag(self):
        pass

    def on_drop_after(self):
        pass

    def on_drop_below(self):
        pass
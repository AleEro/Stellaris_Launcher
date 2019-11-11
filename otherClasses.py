from PyQt5 import QtWidgets, QtCore, QtGui


class Mod():
    def __init__(self, mod_hash, gameRegistryId, source, steamId, displayName, tags, requiredVersion,
                 archivePath, status, Mid, timeUpdated, thumbnailUrl, dirPath, thumbnailPath):
        self.mod_hash = mod_hash
        self.gameRegistryId = gameRegistryId
        self.source = source
        self.steamId = steamId
        self.displayName = displayName
        self.tags = tags
        self.requiredVersion = requiredVersion
        self.archivePath = archivePath
        self.status = status
        self.Mid = Mid
        self.timeUpdated = timeUpdated
        self.thumbnailUrl = thumbnailUrl
        self.dirPath = dirPath
        self.thumbnailPath = thumbnailPath


class TableData(QtGui.QStandardItemModel):
    def __init__(self, root, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root

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
        self.setGridStyle(QtCore.Qt.NoPen)
        self.setShowGrid(False)

    def on_drag(self):
        pass

    def on_drop_after(self):
        pass

    def on_drop_below(self):
        pass

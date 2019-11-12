from PyQt5 import QtWidgets, QtCore, QtGui


class Button(QtWidgets.QPushButton):
    def __init__(self, text='Button', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText(text)
        self.setFlat(True)


class Mod():
    def __init__(self, mod_hash, mod_data):
        empt = '-'
        self.mod_hash         = mod_hash
        self.mod_data         = mod_data

        self.gameRegistryId   = mod_data['gameRegistryId']  if 'gameRegistryId'  in mod_data else empt
        self.source           = mod_data['source']          if 'source'          in mod_data else empt
        self.steamId          = mod_data['steamId']         if 'steamId'         in mod_data else empt
        self.displayName      = mod_data['displayName']     if 'displayName'     in mod_data else empt
        self.tags             = mod_data['tags']            if 'tags'            in mod_data else empt
        self.requiredVersion  = mod_data['requiredVersion'] if 'requiredVersion' in mod_data else empt
        self.archivePath      = mod_data['archivePath']     if 'archivePath'     in mod_data else empt
        self.status           = mod_data['status']          if 'status'          in mod_data else empt
        self.Mid              = mod_data['Mid']             if 'Mid'             in mod_data else empt
        self.timeUpdated      = mod_data['timeUpdated']     if 'timeUpdated'     in mod_data else empt
        self.thumbnailUrl     = mod_data['thumbnailUrl']    if 'thumbnailUrl'    in mod_data else empt
        self.dirPath          = mod_data['dirPath']         if 'dirPath'         in mod_data else empt
        self.thumbnailPath    = mod_data['thumbnailPath']   if 'thumbnailPath'   in mod_data else empt


class TableData(QtGui.QStandardItemModel):
    def __init__(self, root, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root
        self.setHorizontalHeaderLabels(['gameRegistryId', 'source', 'steamId', 'displayName', 'tags',
                                        'requiredVersion', 'archivePath', 'status', 'id', 'timeUpdated',
                                        'thumbnailUrl', 'dirPath', 'thumbnailPath'])

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
        self.setDragDropMode(self.DragOnly)
        self.setDragEnabled(True)
        self.setGridStyle(QtCore.Qt.NoPen)
        self.setShowGrid(False)

    def on_drag(self):
        pass

    def on_drop_after(self):
        pass

    def on_drop_below(self):
        pass
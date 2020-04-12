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


class TableDataItem(QtGui.QStandardItemModel):

    def dropMimeData(self, data, action, row, col, parent):
        """
        Always move the entire row, and don't allow column "shifting"
        """
        return super().dropMimeData(data, action, row, 0, parent)


class PStyle(QtWidgets.QProxyStyle):

    def drawPrimitive(self, element, option, painter, widget=None):
        """
        Draw a line across the entire row rather than just the column
        we're hovering over.  This may not always work depending on global
        style - for instance I think it won't work on OSX.
        """
        if element == self.PE_IndicatorItemViewItemDrop and not option.rect.isNull():
            option_new = QtWidgets.QStyleOption(option)
            option_new.rect.setLeft(0)
            if widget:
                option_new.rect.setRight(widget.width())
            option = option_new
        super().drawPrimitive(element, option, painter, widget)


class TableData(QtGui.QStandardItemModel):
    def __init__(self, root, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root
        self.setHorizontalHeaderLabels([
            'gameRegistryId', 'source', 'steamId', 'displayName', 'tags',
                                        'requiredVersion', 'archivePath', 'status', 'id', 'timeUpdated',
                                        'thumbnailUrl', 'dirPath', 'thumbnailPath'])

    def dropMimeData(self, data, action, row, col, parent):
        return super().dropMimeData(data, action, row, 0, parent)


class Table(QtWidgets.QTableView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sim = TableData(self)
        self.setModel(self.sim)

        self.setShowGrid(False)
        self.setGridStyle(QtCore.Qt.NoPen)

        # self.setSelectionMode(self.SingleSelection)
        self.setSelectionBehavior(self.SelectRows)
        self.setEditTriggers(self.NoEditTriggers)

        self.setDragEnabled(True)
        self.setDragDropMode(self.InternalMove)
        self.setDragDropOverwriteMode(False)

        # self.verticalHeader().hide()
        # self.horizontalHeader().hide()
        self.setStyle(PStyle())

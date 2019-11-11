from PyQt5 import QtWidgets, QtCore, QtGui


class TableData(QtGui.QStandardItemModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


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

    def on_drop(self):
        pass

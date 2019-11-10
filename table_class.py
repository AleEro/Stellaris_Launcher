from PyQt5 import QtWidgets, QtCore


class Table(QtWidgets.QTableWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # elements
        ab_st = QtWidgets.QAbstractItemView
        self.setSelectionMode(ab_st.SingleSelection)
        self.setSelectionBehavior(ab_st.SelectRows)
        self.setEditTriggers(ab_st.NoEditTriggers)
        self.setDragDropMode(ab_st.InternalMove)
        self.setDragEnabled(True)
        self.setColumnCount(4)
        self.setRowCount(4)
        self.setGridStyle(QtCore.Qt.NoPen)
        self.setShowGrid(False)

    def on_drag(self):
        pass

    def on_drop(self):
        pass
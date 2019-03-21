import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore
import csv


class MyWindow(QtGui.QWidget):
    def __init__(self, fileName, parent=None):
        super(MyWindow, self).__init__(parent)
        self.fileName = fileName

        self.model = QtGui.QStandardItemModel(self)

        self.tableView = QtGui.QTableView(self)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.pushButtonLoad = QtGui.QPushButton(self)
        self.pushButtonLoad.setText("Load Csv File!")
        self.pushButtonLoad.clicked.connect(self.on_pushButtonLoad_clicked)

        self.pushButtonWrite = QtGui.QPushButton(self)
        self.pushButtonWrite.setText("Write Csv File!")
        self.pushButtonWrite.clicked.connect(self.on_pushButtonWrite_clicked)

        self.layoutVertical = QtGui.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.tableView)
        self.layoutVertical.addWidget(self.pushButtonLoad)
        self.layoutVertical.addWidget(self.pushButtonWrite)

    def loadCsv(self, fileName):
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput):
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)

    def writeCsv(self, fileName):
        with open(fileName, "w",newline='') as fileOutput:
            writer = csv.writer(fileOutput)
            for rowNumber in range(self.model.rowCount()):
                fields = [
                    self.model.data(
                        self.model.index(rowNumber,columnNumber),
                        QtCore.Qt.DisplayRole
                    )
                    for columnNumber in range(self.model.columnCount())
                ]
                writer.writerow(fields)

    def on_pushButtonWrite_clicked(self):
        self.writeCsv(self.fileName)

    def on_pushButtonLoad_clicked(self):
        self.loadCsv(self.fileName)

#
# app = QtGui.QApplication(sys.argv)
# app.setApplicationName('MyWindow')
#
# main = MyWindow("e://personal/Github/pyqt/csvsample.csv")
# main.show()
#
# sys.exit(app.exec_())
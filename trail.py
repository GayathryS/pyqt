import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
import csv


class csvWindow(QWidget):
    def __init__(self,parent=None):
        super(csvWindow,self).__init__(parent)
        self.csvlayout = QtGui.QVBoxLayout(self)


class filedialogdemo(QWidget):
    def __init__(self, parent=None):

        super(filedialogdemo, self).__init__(parent)
        # self.mdi = QMdiArea()
        # self.setCentralWidget(self.mdi)
        layout = QVBoxLayout()
        self.btn = QPushButton("Open CSV File")
        self.btn.clicked.connect(self.getfile)
        layout.addWidget(self.btn)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)
        self.setLayout(layout)
        self.setWindowTitle("Select the csv file")

    def getfile(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file',
                                            'e:\\personal\Github\pyqt', "CSV files (*.csv)")
        rows = []

        # reading csv file
        with open(filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)
            print(rows)
            self.table = QTableWidget(len(rows), len(rows[0]), self)
            for column in range(len(rows[0]) - 1):
                for row in range(len(rows) - 1):
                    item = QTableWidgetItem(rows[row][column])
                    self.table.setItem(row, column, item)

            self.dialog = csvWindow(self)
            self.dialog.csvlayout.addWidget(self.table)
            self.dialog.show()

            # sub = QMdiSubWindow()
            # sub.setWidget(self.table)
            #
            # sub.setWindowTitle("subwindow")
            # self.mdi.addSubWindow(sub)
            # sub.show()


def main():
    app = QApplication(sys.argv)
    ex = filedialogdemo()
    ex.show()
    sys.exit(app.exec_())

main()
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import csv
import pandas
import matplotlib.pyplot as plt
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.filename = ''
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        self.model = QStandardItemModel(self)
        self.tableView = QTableView(self.mdi)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.setCentralWidget(self.tableView)

        self.tableView.move(1000,200)

        self.tableView.clicked.connect(self.cellClickx)
        self.tableView.clicked.connect(self.cellClicky)

        self.win = QDialog()

        self.button = QPushButton('Plot scatter point', self)
        self.button.resize(250, 50)
        self.button.move(50, 50)
        self.button.clicked.connect(self.paintEvent(self.event))
        self.button = QPushButton('Plot scatter point with smooth lines', self)
        self.button.resize(250,50)
        self.button.move(300, 50)
        self.button.clicked.connect(self.p2)
        self.button = QPushButton('Plot lines', self)
        self.button.resize(250, 50)
        self.button.move(550, 50)
        self.button.clicked.connect(self.p3)

        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("Load")
        edit = bar.addMenu("Edit")
        edit.addAction("Edit data")
        file.addAction("Add data")
        file.addAction("Save")
        file.addAction("Save as PNG")
        self.setWindowTitle("Main Window")
        file.triggered[QAction].connect(self.windowaction)

    def paintEvent(self,e):
        self.qp = QPainter()
        self.qp.begin(self)
        self.qp.drawPoints(self.qp)
        # self.qp.end()

    def drawPoints(self,qp):

        self.qp.setPen(Qt.red)
        #size = self.size()
        self.qp.drawPoint(self.x,self.y)

    def p1(self):
        #self.win.show()
        self.sub = QMdiSubWindow()
        self.sub.setGeometry(300, 300, 280, 170)
        self.sub.setWindowTitle('Points')

        ax = plt.axes()
        x=[1,2,3,4,5]
        y=[1,2,3,4,5]
        plt.scatter(x,y)
        plt.show()
        self.show()

    def p2(self):
        self.win.show()
        fig = plt.figure()
        ax = plt.axes()
        plt.plot(x, y)

    def p3(self):
        self.win.show()


    def cellClickx(self,item):
        print("hi")
        self.x=item.column
        print(self.x)
    def cellClicky(self,item):
        self.y=item.column
        print(self.y)
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
                print(fields)
                writer.writerow(fields)

    def loadCsv(self, fileName):
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput):
                items = [
                    QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)

    def windowaction(self, q):
        if q.text() == "Load":
            filename = QFileDialog.getOpenFileName(self, 'Open file',
                                                   'e:\\personal\Github\pyqt', "CSV files (*.csv)")
            print(filename)
            self.filename = filename
            self.loadCsv(self.filename)
            data = pandas.read_csv(self.filename)
            # x=input("enter column names to be plotted as x axis")
            # y = input("enter column names to be plotted as y axis")

        elif q.text() == "Edit data":
            self.filename=filename
            self.writeCsv(self.filename)
        elif q.text() == "Add data":
            self.model.appendRow([])
        elif q.text() == "Save":
            self.writeCsv(self.filename)


def main():
    app = QApplication(sys.argv)

    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


main()
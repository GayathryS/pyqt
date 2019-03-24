import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from csvfinal import *
from plt import *
import matplotlib.pyplot as plt
import pandas


filename = "e:\\personal\Github\pyqt\csvsample.csv"


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui()
        self.ui.setupUi(self)
        self.createtable()

        self.filename = ''
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        self.model = QtGui.QStandardItemModel(self)
        self.tableView = QtGui.QTableView(self.mdi)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.setCentralWidget(self.tableView)
        # self.tableView.isFullScreen()
        # self.tableView.showFullScreen()
        # b1 = QPushButton(win)
        # b1.setText("Plot scatter point")
        # b1.move(50, 20)
        # b1.clicked.connect(b1_clicked)

        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("Load")
        edit = bar.addMenu("Edit")
        edit.addAction("Edit data")
        file.addAction("Add data")
        #data.addAction("Row")
       # data.addAction("Column")
        file.addAction("Save")
        file.addAction("Save as PNG")
        self.setWindowTitle("Main Window")
        file.triggered[QAction].connect(self.windowaction)

        # self.layoutVertical = QtGui.QVBoxLayout(self)
        # self.layoutVertical.addWidget(self.tableView)
        # b2 = QPushButton(win)
        # b2.setText("Plot scatter point with smooth lines")
        # b2.move(50, 50)
        # b2.clicked.connect(b1_clicked)

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
                    QtGui.QStandardItem(field)
                    for field in row
                ]

                self.model.appendRow(items)

    def windowaction(self, q):
        if q.text() == "Load":
            filename = QFileDialog.getOpenFileName(self, 'Open file',
                                                   'e:\\personal\Github\pyqt', "CSV files (*.csv)")
            print(filename)
            self.filename = filename
           # self.loadCsv(self.filename)
            self.createtable()
            print("finished")


        elif q.text()=="Edit data":
            with open(fileName, "w", newline='') as fileOutput:
                writer = csv.writer(fileOutput)
                for rowNumber in range(self.model.rowCount()):
                    fields = [
                        self.model.data(
                            self.model.index(rowNumber, columnNumber),
                            QtCore.Qt.DisplayRole
                        )
                        for columnNumber in range(self.model.columnCount())
                    ]
                    print(fields)
                    writer.writerow(fields)
        elif q.text() == "Add data":
       # elif q.text() == "Row":
            self.model.appendRow([])
        #elif q.text() == "Column":
          #  self.model.appendColumn([])
        elif q.text() == "Save":
            self.writeCsv(self.filename)
        elif q.text() == "Save as PNG":
            p = QPixmap.grabWindow(QTableView.winId())
            p.save(filename, 'jpg')


def main():
    app = QApplication(sys.argv)

    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

# def b1_clicked():
#     plt.scatter(x,y)
#
#
# def b2_clicked():
#     plt.plot(x,y,'-','linewidth',2)

    #creating a tw cell
def cell(self,var=""):
    item = QtGui.QTableWidgetItem()
    item.setText(var)
    return item


def createtable(self):

    rows = self.tableName.rowCount()
    columns = self.tableName.columnCount()
    with open(fileName, "r") as fileInput:
        for i in range(rows):
            for j in range(columns):
                item = self.cell(fileInput)
                self.ui.tableName.setItem(i, j, item)


main()




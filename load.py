import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import csv

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
      super(MainWindow, self).__init__(parent)

      self.mdi = QMdiArea()
      self.setCentralWidget(self.mdi)
      bar = self.menuBar()
      file = bar.addMenu("File")
      file.addAction("Load")
      edit = bar.addMenu("Edit")
      edit.addAction("Edit data")
      file.addAction("Add data")
      file.addAction("Save as PNG")
      self.setWindowTitle("Main WIndow")

      layout = QVBoxLayout()
      self.btn = QPushButton("Select the csv file")
      self.btn.clicked.connect(self.getfile)
      layout.addWidget(self.btn)

      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.setLayout(layout)
      self.setWindowTitle("Choose file")
    def getfile(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "CSV files (*.csv)")

    def windowaction(self, q):
      print ("triggered")
      if q.text=="Load":
          self.getfile()
      if q.text=="Edit data":
        #to be completed
        pass
      if q.text=="Add data":
        #to be completed
        pass
      if q.text=="Save as PNG":
        pass
        #to be completed
def main():
   app = QApplication(sys.argv)
   
   ex = MainWindow()
   ex.show()
   sys.exit(app.exec_())


main()




import matplotlib.pyplot as plt
import pandas
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
def window():
   app = QApplication(sys.argv)
   win = QDialog()
   b1 = QPushButton(win)
   b1.setText("Plot scatter point")
   b1.move(50,20)
   b1.clicked.connect(b1_clicked)

   b2 = QPushButton(win)
   b2.setText("Plot scatter point with smooth lines")
   b2.move(50, 50)
   b2.clicked.connect(b1_clicked)

   win.setGeometry(100, 100, 200, 100)
   win.setWindowTitle("PyQt")
   win.show()
   sys.exit(app.exec_())


def b1_clicked():
    plt.scatter(x,y)


def b2_clicked():
    plt.plot(x,y,'-','linewidth',2)


window()
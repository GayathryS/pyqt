import sys
from PyQt4 import QtGui

print("entered function")
app = QtGui.QApplication(sys.argv)
print("app created")
w = QtGui.QWidget()
print("widget created")
b = QtGui.QLabel(w)
b.setText("Hello World!")
w.setGeometry(100,100,200,50)
b.move(50,20)
w.setWindowTitle("PyQt")
w.show()
sys.exit(app.exec_())

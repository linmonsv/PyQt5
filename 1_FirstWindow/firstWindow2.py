from PyQt5 import QtWidgets

class mywindow(QtWidgets.QWidget):
    def __init__(self):
        super(mywindow,self).__init__()

import sys
app=QtWidgets.QApplication(sys.argv)
windows=mywindow()
label=QtWidgets.QLabel(windows)
label.setText("hello world!")

windows.show()
sys.exit(app.exec_())

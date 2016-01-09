from PyQt5 import QtWidgets
from untitled import Ui_Form

import re, sip
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class mywindow(QtWidgets.QWidget):
    def __init__(self):
        super(mywindow,self).__init__()
        self.new=Ui_Form()
        self.new.setupUi(self)

if __name__=="__main__":
    import sys

    app=QtWidgets.QApplication(sys.argv)
    myshow=mywindow()
    myshow.show()
    sys.exit(app.exec_())

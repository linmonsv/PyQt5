from PyQt5 import QtWidgets
from untitled import Ui_Form

class mywindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)

if __name__=="__main__":
    import sys

    app=QtWidgets.QApplication(sys.argv)
    myshow=mywindow()
    myshow.show()
    sys.exit(app.exec_())

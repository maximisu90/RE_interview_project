import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication, QMainWindow)
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont

class basicWindow(QWidget):
    def __init__(self):
        super().__init__()
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)
        validator=QIntValidator(240,2400)
        self.qline=QtWidgets.QLineEdit()
        self.qline.setText('20')
        self.qline.editingFinished.connect(self.check_validation)
        self.qline.setValidator(validator)

        self.but=QPushButton()
        self.but.clicked.connect(self.printifvalid)


        grid_layout.addWidget(self.qline,0,0)
        grid_layout.addWidget(self.but,1,0)

    def printifvalid(self):
        if self.qline.hasAcceptableInput():
            print(self.qline.validator().top())
    def check_validation(self):
        print(self.qline.hasAcceptableInput())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowExample = basicWindow()
    windowExample.show()
    sys.exit(app.exec_())
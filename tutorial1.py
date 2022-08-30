import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication, QMainWindow)
from PyQt5 import QtWidgets, QtGui

class v_current_value(QtWidgets.QLabel):
    def __init__(self,name='',):
        super().__init__()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)
        self.setAutoFillBackground(True)
        self.setFrameShape(QtWidgets.QFrame.Panel)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.setMidLineWidth(2)
        self.setObjectName(name)
        self.setText('0')
        color  = QtGui.QColor(0,255,0)
        alpha  = 140
        values = "{r}, {g}, {b}, {a}".format(r = color.red(),
                                            g = color.green(),
                                            b = color.blue(),
                                            a = alpha
                                            )
        self.setStyleSheet("QLabel { background-color: rgba("+values+"); }")
    def update_val(self,value='0'):
        self.setText(value)


class v_set_point(QtWidgets.QLineEdit):
    def __init__(self,name='',):
        super().__init__()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)
        self.setAutoFillBackground(True)
        

        self.setObjectName(name)
        self.setText('0')
        color  = QtGui.QColor(255,255,255)
        alpha  = 140
        values = "{r}, {g}, {b}, {a}".format(r = color.red(),
                                            g = color.green(),
                                            b = color.blue(),
                                            a = alpha
                                            )
        self.setStyleSheet("QLabel { background-color: rgba("+values+"); }")
    def get_value(self):
        return(self.text())


class v_set_point_list(QtWidgets.QComboBox):
    def __init__(self,name='',value_list=[]):
        super().__init__()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)
        
        self.setObjectName(name)
        self.addItems(value_list)
        color  = QtGui.QColor(255,255,255)
        alpha  = 140
        values = "{r}, {g}, {b}, {a}".format(r = color.red(),
                                            g = color.green(),
                                            b = color.blue(),
                                            a = alpha
                                            )
        self.setStyleSheet("QLabel { background-color: rgba("+values+"); }")
    def get_value(self):
        return(self.currentText())


class v_set_button(QtWidgets.QPushButton):
    def __init__(self,name='',):
        super().__init__()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)
        self.setAutoFillBackground(True)
        self.setObjectName(name)
        self.setText('Set')
        color  = QtGui.QColor(0,0,255)
        alpha  = 140
        values = "{r}, {g}, {b}, {a}".format(r = color.red(),
                                            g = color.green(),
                                            b = color.blue(),
                                            a = alpha
                                            )
        self.setStyleSheet("QLabel { background-color: rgba("+values+"); }")


class basicWindow(QWidget):
    def __init__(self):
        super().__init__()
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        v_names=[QtWidgets.QLabel("Beamline energy eV"),
        QtWidgets.QLabel("Harmonic"),
        QtWidgets.QLabel("Exit slit, \u03BCm"),
        QtWidgets.QLabel("Beamline resolution, meV")]

        self.v_current_vals=[v_current_value(name='cur1'),
        v_current_value(name='cur2'),
        v_current_value(name='cur3'),
        v_current_value(name='cur4')]


        self.v_set_points=[v_set_point(name='set1'),
        v_set_point_list(name='set2',value_list=["1st","3rd"]),
        v_set_point(name='set3'),
        v_set_point(name='set4')]

        v_set_buttons=[v_set_button(name='Bset1'),
        v_set_button(name='Bset2'),
        v_set_button(name='Bset3'),
        v_set_button(name='Bset4')]


        grid_layout.addWidget(QtWidgets.QLabel("Beamline"),0,0)

        for x in range(4):
            grid_layout.addWidget(v_names[x], x+1, 0)
        
        

        for x in range(4):
            grid_layout.addWidget(self.v_current_vals[x], x+1, 1)
       
        for x in range(4):
            grid_layout.addWidget(self.v_set_points[x], x+1, 2)

        for x in range(4):
            grid_layout.addWidget(v_set_buttons[x], x+1, 3)
        
        self.setWindowTitle('Basic Grid Layout')

        for i in range(4):

            v_set_buttons[i].clicked.connect(lambda _, i=i: self.set_value(i))

    


    def set_value(self,i):
        val=self.v_set_points[i].get_value()
        self.v_current_vals[i].update_val(val)

        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowExample = basicWindow()
    windowExample.show()
    sys.exit(app.exec_())

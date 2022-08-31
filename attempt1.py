import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication, QMainWindow)
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont

class Labels(QtWidgets.QLabel):
    def __init__(self,name='',txt=''):
        super().__init__()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)
        self.setAutoFillBackground(True)
        
        self.setObjectName(name)
        self.setText(txt)
        color  = QtGui.QColor(255,255,255)
        alpha  = 140
        values = "{r}, {g}, {b}, {a}".format(r = color.red(),
                                            g = color.green(),
                                            b = color.blue(),
                                            a = alpha
                                            )


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

        #Beamline part
        self.b_names=[Labels(name='label1',txt="Beamline energy eV"),
        Labels(name='label2',txt="Harmonic"),
        Labels(name='label3',txt="Exit slit, \u03BCm"),
        Labels(name='label4',txt="Beamline resolution, meV")]

        self.b_current_vals=[v_current_value(name='cur1'),
        v_current_value(name='cur2'),
        v_current_value(name='cur3'),
        v_current_value(name='cur4')]


        self.b_set_points=[v_set_point(name='Beamline energy'),
        v_set_point_list(name='Harmonic',value_list=["1st","3rd"]),
        v_set_point(name='Exit slit'),
        v_set_point(name='Beamline resolution')]

        self.b_set_points[0].setValidator(QIntValidator(240,2400))

        self.b_set_buttons=[v_set_button(name='Beamline energy'),
        v_set_button(name='Harmonic'),
        v_set_button(name='Exit slit'),
        v_set_button(name='Beamline resolution')]


        grid_layout.addWidget(Labels(name='label5',txt="Beamline"),0,0)

        for x in range(4):
            grid_layout.addWidget(self.b_names[x], x+1, 0)
        
        

        for x in range(4):
            grid_layout.addWidget(self.b_current_vals[x], x+1, 1)
       
        for x in range(4):
            grid_layout.addWidget(self.b_set_points[x], x+1, 2)

        for x in range(4):
            grid_layout.addWidget(self.b_set_buttons[x], x+1, 3)
        
        self.setWindowTitle('Basic Grid Layout')

        for i in range(4):
            self.b_set_buttons[i].clicked.connect(lambda _, i=i: self.set_b_value(i))

        spacer_item2 = QtWidgets.QSpacerItem(20, 50)
        grid_layout.addItem(spacer_item2)
        grid_layout.addWidget(Labels(name='label6',txt="Analyzer"),6,0)

        
        #Analyzer part
        self.a_names=[Labels(name='label1',txt="Analyzer slit, mm"),
        Labels(name='label2',txt="Pass Energy, eV"),
        Labels(name='label3',txt="Analyzer resolution")]

        self.a_current_vals=[v_current_value(name='acur1'),
        v_current_value(name='acur2'),
        v_current_value(name='acur3')]


        self.a_set_points=[v_set_point_list(name='aset1',value_list=["1.5", "0.8", "0.4", "0.2"]),
        v_set_point_list(name='aset2',value_list=["1","2","5","10","20","50","100","200"]),
        v_set_point(name='aset3')]

        self.a_set_buttons=[v_set_button(name='aBset1'),
        v_set_button(name='aBset2'),
        v_set_button(name='aBset3')]

        

        for x in range(3):
            grid_layout.addWidget(self.a_names[x], x+7, 0)
        
        

        for x in range(3):
            grid_layout.addWidget(self.a_current_vals[x], x+7, 1)
       
        for x in range(3):
            grid_layout.addWidget(self.a_set_points[x], x+7, 2)

        for x in range(3):
            grid_layout.addWidget(self.a_set_buttons[x], x+7, 3)
        
        for i in range(3):
            self.a_set_buttons[i].clicked.connect(lambda _, i=i: self.set_a_value(i))

    def set_b_value(self,i):
        val=self.b_set_points[i].get_value()
        
        self.b_current_vals[i].update_val(val)

    def set_a_value(self,i):
        val=self.a_set_points[i].get_value()
        self.a_current_vals[i].update_val(val)
    def validate_input(self,set_val):
        print('validating')
        if set_val.name=='Beamline energy':
            val=float(set_val.get_value())
            if (val<250)&(val>2400):
                print('Bubu la beam energy')
        
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowExample = basicWindow()
    windowExample.show()
    sys.exit(app.exec_())

import sys
from turtle import onclick
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication, QMainWindow)
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
import numpy as np

class Parameter_list():
    def __init__(self,name='',current_val='12',value_list=['12','13']):
        font = QtGui.QFont()
        font.setPointSize(12)
        
        
            
        self.label=QtWidgets.QLabel()
        self.label.setText(name)
        self.label.setFont(font)

        self.curr_val=QtWidgets.QLabel()
        self.curr_val.setFont(font)
        self.curr_val.setAutoFillBackground(True)
        self.curr_val.setFrameShape(QtWidgets.QFrame.Panel)
        self.curr_val.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.curr_val.setMidLineWidth(2)

        self.curr_val.setText(current_val)
        color  = QtGui.QColor(0,255,0)
        alpha  = 140
        values = "{r}, {g}, {b}, {a}".format(r = color.red(),
                                            g = color.green(),
                                            b = color.blue(),
                                            a = alpha
                                            )
        self.curr_val.setStyleSheet("QLabel { background-color: rgba("+values+"); }")


        self.set_val=QtWidgets.QComboBox()
        self.set_val.setFont(font)
        self.set_val.setAutoFillBackground(True)
        self.set_val.addItems(value_list)
        color  = QtGui.QColor(255,255,255)
        alpha  = 140
        values = "{r}, {g}, {b}, {a}".format(r = color.red(),
                                            g = color.green(),
                                            b = color.blue(),
                                            a = alpha
                                            )
        self.set_val.setStyleSheet("QLabel { background-color: rgba("+values+"); }")
        

        self.set_button=QtWidgets.QPushButton()
        self.set_button.setFont(font)
        self.set_button.setAutoFillBackground(True)
        self.set_button.setObjectName(name)
        self.set_button.setText('Set')
        color  = QtGui.QColor(0,0,255)
        alpha  = 140
        values = "{r}, {g}, {b}, {a}".format(r = color.red(),
                                            g = color.green(),
                                            b = color.blue(),
                                            a = alpha
                                            )
        self.set_button.setStyleSheet("QLabel { background-color: rgba("+values+"); }")

        self.onclick()
    def onclick(self):
        self.set_button.clicked.connect(self.set_value)
    def set_value(self):            
        val=self.set_val.currentText()
        self.curr_val.setText(val)


class Parameter():
    def __init__(self,name='',current_val='12',set_val='12',validator=None,val_top=123154,val_bottom=-12314):
        font = QtGui.QFont()
        font.setPointSize(12)
        
        
        
        self.label=QtWidgets.QLabel()
        self.label.setText(name)
        self.label.setFont(font)

        self.curr_val=QtWidgets.QLabel()
        self.curr_val.setFont(font)
        self.curr_val.setAutoFillBackground(True)
        self.curr_val.setFrameShape(QtWidgets.QFrame.Panel)
        self.curr_val.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.curr_val.setMidLineWidth(2)

        self.curr_val.setText(current_val)
        color  = QtGui.QColor(0,255,0)
        alpha  = 140
        values = "{r}, {g}, {b}, {a}".format(r = color.red(),
                                            g = color.green(),
                                            b = color.blue(),
                                            a = alpha
                                            )
        self.curr_val.setStyleSheet("QLabel { background-color: rgba("+values+"); }")


        self.set_val=QtWidgets.QLineEdit()
        self.set_val.setFont(font)
        self.set_val.setAutoFillBackground(True)
        self.set_val.setText(set_val)
        color  = QtGui.QColor(255,255,255)
        alpha  = 140
        values = "{r}, {g}, {b}, {a}".format(r = color.red(),
                                            g = color.green(),
                                            b = color.blue(),
                                            a = alpha
                                            )
        self.set_val.setStyleSheet("QLabel { background-color: rgba("+values+"); }")
        if validator!=None:
            self.set_val.setValidator(QIntValidator(val_bottom,val_top))

        self.set_button=QtWidgets.QPushButton()
        self.set_button.setFont(font)
        self.set_button.setAutoFillBackground(True)
        self.set_button.setObjectName(name)
        self.set_button.setText('Set')
        color  = QtGui.QColor(0,0,255)
        alpha  = 140
        values = "{r}, {g}, {b}, {a}".format(r = color.red(),
                                            g = color.green(),
                                            b = color.blue(),
                                            a = alpha
                                            )
        self.set_button.setStyleSheet("QLabel { background-color: rgba("+values+"); }")

        self.onclick()
    def onclick(self):
        self.set_button.clicked.connect(self.set_b_value)
    def set_b_value(self):            
        if 'hasAcceptableInput' in dir(self.set_val):
            if self.set_val.hasAcceptableInput():
                val=self.set_val.text()
                self.curr_val.setText(val)
            else:
                print('Value outside range ',self.set_val.validator().bottom(),' and ',self.set_val.validator().top())
        else:
            val=self.set_val.text()
            self.curr_val.setText(val)
    def get_cur_val(self):
        return self.curr_val.text()
    
class business_logic():
    data=np.loadtxt('slit_energy_data.txt',skiprows=1)
    def __init__(self,parameters=[],clicked_par_key='Beamline energy') :
        a=1
        
        # if clicked_par_key=='Beamline energy':


        



class basicWindow(QWidget):

    
    def __init__(self):
        super().__init__()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        section_beamline=QtWidgets.QLabel('Beamline')
        section_beamline.setFont(font)

        self.par={'Beamline energy':[],
        "Harmonic":[],'Exit slit':[],
        "Beamline resolution":[],
        'Analyzer slit':[],
         "Pass energy":[],
         "Analyzer resolution":[] }

        self.grid_layout.addWidget(section_beamline,0,0)
        self.par['Beamline energy']=Parameter(name='Beamline energy eV',validator=QIntValidator,val_bottom=240,val_top=2400)
        self.par["Harmonic"]=Parameter_list(name= "Harmonic",current_val='1st',value_list=['1st','3rd'])
        self.par['Exit slit']=Parameter(name= "Exit slit, \u03BCm",validator=QDoubleValidator,val_bottom=-5,val_top=500)
        self.par["Beamline resolution"]=Parameter(name= "Beamline resolution",validator=QIntValidator,val_bottom=1,val_top=123456)
        self.ad_par_layout(self.par['Beamline energy'],1)
        self.ad_par_layout(self.par["Harmonic"],2)
        self.ad_par_layout(self.par['Exit slit'],3)
        self.ad_par_layout(self.par["Beamline resolution"],4)

        section_analyzer=QtWidgets.QLabel('Analyzer')
        section_analyzer.setFont(font)
        self.grid_layout.addWidget(section_analyzer,5,0)


        self.par['Analyzer slit']=Parameter_list(name='Analyzer slit',current_val='1.5',value_list=["1.5", "0.8", "0.4", "0.2"])
        self.par["Pass energy"]=Parameter_list(name= "Pass energy eV",current_val='1',value_list=["1","2","5","10","20","50","100","200"])
        self.par["Analyzer resolution"]=Parameter(name= "Analyzer resolution",validator=QIntValidator,val_bottom=1,val_top=123456)
        self.ad_par_layout(self.par['Analyzer slit'],6)
        self.ad_par_layout(self.par["Pass energy"],7)
        self.ad_par_layout(self.par["Analyzer resolution"],8)
        


    def ad_par_layout(self,par,nrow):
        self.grid_layout.addWidget(par.label,nrow,0)
        self.grid_layout.addWidget(par.curr_val,nrow,1)
        self.grid_layout.addWidget(par.set_val,nrow,2)
        self.grid_layout.addWidget(par.set_button,nrow,3)
    
    

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # windowExample = basicWindow()
    # windowExample.show()
    # sys.exit(app.exec_())
    a=business_logic()
    print(a.data[1,1]/2)
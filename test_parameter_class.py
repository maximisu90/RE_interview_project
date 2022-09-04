import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,QPushButton, QApplication, QMainWindow)
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
import numpy as np
from scipy.interpolate import interp1d

from parameters import Parameter, Parameter_combined_resolution, Parameter_list
    
class business_logic():
    
    def __init__(self,parameters=[],clicked_par_key='Beamline energy') :
        self.parameters=parameters
        self.clicked_par_key=clicked_par_key
        data=np.loadtxt('slit_energy_data.txt',skiprows=1)
        self.R=data[:,1]
        self.Exit_slit=data[:,0]
        self.interp_exit_slit=interp1d(self.Exit_slit,1/self.R)
        self.interp_bl_resolution=interp1d(self.R,1/self.Exit_slit)
    def apply_logic_bl_energy(self):
        if (float(self.parameters['Beamline energy'].get_cur_val())>1200)&(self.parameters['Harmonic'].curr_val.text()=='1st'):
            self.parameters['Harmonic'].set_val.setCurrentIndex(1)
            self.parameters['Harmonic'].curr_val.setText('3rd')
        elif (float(self.parameters['Beamline energy'].get_cur_val())<=1200)&(self.parameters['Harmonic'].curr_val.text()=='3rd'):
            self.parameters['Harmonic'].set_val.setCurrentIndex(0)
            self.parameters['Harmonic'].curr_val.setText('1st')

    def apply_logic_exit_slit(self):        
        val=float(self.parameters['Exit slit'].curr_val.text())
        R_interp=int(1/self.interp_exit_slit(val))
        E=float(self.parameters['Beamline energy'].curr_val.text())
        dE=int(E/R_interp*1e3)
        self.parameters["Beamline resolution"].curr_val.setText(f'{dE}')
        self.parameters["Beamline resolution"].set_val.setText(f'{dE}')
        self.apply_logic_combined_resolution()

    def apply_logic_bl_res(self):        
        dE=float(self.parameters["Beamline resolution"].curr_val.text())
        E=float(self.parameters['Beamline energy'].curr_val.text())*1e-3
        R=E/dE
        if R<3500:
            Eslit_interp=150
        elif R>30000:
            Eslit_interp=10
        else:
            Eslit_interp=int(1/self.interp_bl_resolution(R))
        # print(Eslit_interp)
        self.parameters["Exit slit"].curr_val.setText(f'{Eslit_interp:.0f}')
        self.parameters['Exit slit'].set_val.setText(f'{Eslit_interp:.0f}')
        self.apply_logic_combined_resolution()

    def apply_logic_pass_energy(self):        
        PE=int(self.parameters["Pass energy"].curr_val.text())
        d=float(self.parameters["Analyzer slit"].curr_val.text())
        dE=int(PE*d/300*1e3)
        self.parameters["Analyzer resolution"].curr_val.setText(f'{dE}')
        self.parameters['Analyzer resolution'].set_val.setText(f'{dE}')
        self.apply_logic_combined_resolution()

    def apply_logic_analyzer_res(self):        
        dE=int(self.parameters["Analyzer resolution"].curr_val.text())
        d=float(self.parameters["Analyzer slit"].curr_val.text())
        PE=dE*1e-3*300/d
        self.parameters["Analyzer resolution"].curr_val.setText(f'{dE}')
        self.parameters['Analyzer resolution'].set_val.setText(f'{dE}')

        self.apply_logic_combined_resolution()


    def apply_logic_combined_resolution(self):
        RB=float(self.parameters["Beamline resolution"].curr_val.text())
        RA=float(self.parameters["Analyzer resolution"].curr_val.text())
        R=int(np.sqrt(RB**2+RA**2))
        self.parameters["Combined resolution"].curr_val.setText(f'{R}')




        



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
        self.par["Beamline resolution"]=Parameter(name= "Beamline resolution, meV",validator=QIntValidator,val_bottom=1,val_top=30000)
        self.ad_par_layout(self.par['Beamline energy'],1)
        self.ad_par_layout(self.par["Harmonic"],2)
        self.ad_par_layout(self.par['Exit slit'],3)
        self.ad_par_layout(self.par["Beamline resolution"],4)

        
        

        section_analyzer=QtWidgets.QLabel('Analyzer')
        section_analyzer.setFont(font)
        self.grid_layout.addWidget(section_analyzer,5,0)


        self.par['Analyzer slit']=Parameter_list(name='Analyzer slit',current_val='1.5',value_list=["1.5", "0.8", "0.4", "0.2"])
        self.par["Pass energy"]=Parameter_list(name= "Pass energy eV",current_val='1',value_list=["1","2","5","10","20","50","100","200"])
        self.par["Analyzer resolution"]=Parameter(name= "Analyzer resolution, meV",validator=QIntValidator,val_bottom=1,val_top=123456)
        self.par["Combined resolution"]=Parameter_combined_resolution(name= "Combined resolution, meV",current_val='1')
        self.ad_par_layout(self.par['Analyzer slit'],6)
        self.ad_par_layout(self.par["Pass energy"],7)
        self.ad_par_layout(self.par["Analyzer resolution"],8)
        self.grid_layout.addWidget(self.par["Combined resolution"].label,9,0)
        self.grid_layout.addWidget(self.par["Combined resolution"].curr_val,9,1)
        

        self.b_log=business_logic(parameters=self.par)
        self.par['Beamline energy'].set_button.clicked.connect(self.b_log.apply_logic_bl_energy)
        self.par['Exit slit'].set_button.clicked.connect(self.b_log.apply_logic_exit_slit)
        self.par['Beamline resolution'].set_button.clicked.connect(self.b_log.apply_logic_bl_res)
        self.par['Pass energy'].set_button.clicked.connect(self.b_log.apply_logic_pass_energy)

    def do_print(self):
        print('mere')

    def ad_par_layout(self,par,nrow):
        self.grid_layout.addWidget(par.label,nrow,0)
        self.grid_layout.addWidget(par.curr_val,nrow,1)
        self.grid_layout.addWidget(par.set_val,nrow,2)
        self.grid_layout.addWidget(par.set_button,nrow,3)
    
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowExample = basicWindow()
    windowExample.show()
    sys.exit(app.exec_())
    # a=business_logic()
    # print(a.data[1,1]/2)
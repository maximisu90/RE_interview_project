import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QApplication)
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import (QIntValidator, QDoubleValidator)
import numpy as np
from business_logic import business_logic

from parameters import Parameter, Parameter_combined_resolution, Parameter_list        


class BasicWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        section_beamline = QtWidgets.QLabel('Beamline')
        section_beamline.setFont(font)

        self.par = {'Beamline energy': [],
                    "Harmonic": [], 'Exit slit': [],
                    "Beamline resolution": [],
                    'Analyzer slit': [],
                    "Pass energy": [],
                    "Analyzer resolution": []}

        self.grid_layout.addWidget(section_beamline, 0, 0)
        self.par['Beamline energy'] = Parameter(name='Beamline energy eV',
                                                current_val='250',
                                                set_val='250',
                                                validator=QIntValidator,
                                                val_bottom=240, val_top=2400)

        self.par["Harmonic"] = Parameter_list(name="Harmonic", 
                                              current_val='1st',
                                              value_list=['1st', '3rd'])
        self.par['Exit slit'] = Parameter(name="Exit slit, \u03BCm",
                                          validator=QDoubleValidator,
                                          val_bottom=5, val_top=500)

        self.par["Beamline resolution"] = Parameter(name="Beamline resolution, meV",
                                                    validator=QIntValidator,
                                                    val_bottom=1, val_top=30000)
        self.ad_par_layout(self.par['Beamline energy'], 1)
        self.ad_par_layout(self.par["Harmonic"], 2)
        self.ad_par_layout(self.par['Exit slit'], 3)
        self.ad_par_layout(self.par["Beamline resolution"], 4)

        section_analyzer = QtWidgets.QLabel('Analyzer')
        section_analyzer.setFont(font)
        self.grid_layout.addWidget(section_analyzer, 5, 0)

        self.par['Analyzer slit'] = Parameter_list(name='Analyzer slit',
                                                   current_val='1.5',
                                                   value_list=["1.5", "0.8", "0.4", "0.2"])

        self.par["Pass energy"] = Parameter_list(name="Pass energy eV",
                                                 current_val='1',
                                                 value_list=["1", "2", "5", "10", "20", "50", "100", "200"])

        self.par["Analyzer resolution"] = Parameter(name="Analyzer resolution, meV",
                                                    validator=QIntValidator,
                                                    val_bottom=1,val_top=123456)
        self.par["Combined resolution"] = Parameter_combined_resolution(name="Combined resolution, meV",
                                                                        current_val='1')
        self.ad_par_layout(self.par['Analyzer slit'], 6)
        self.ad_par_layout(self.par["Pass energy"], 7)
        self.ad_par_layout(self.par["Analyzer resolution"], 8)
        self.grid_layout.addWidget(self.par["Combined resolution"].label, 9, 0)
        self.grid_layout.addWidget(self.par["Combined resolution"].curr_val, 9, 1)
        

        self.b_log = business_logic(parameters=self.par)
        self.par['Beamline energy'].set_button.clicked.connect(self.b_log.apply_logic_bl_energy)
        self.par['Exit slit'].set_button.clicked.connect(self.b_log.apply_logic_exit_slit)
        self.par['Beamline resolution'].set_button.clicked.connect(self.b_log.apply_logic_bl_res)
        self.par['Pass energy'].set_button.clicked.connect(self.b_log.apply_logic_pass_energy)
        self.par['Analyzer resolution'].set_button.clicked.connect(self.b_log.apply_logic_analyzer_res)

    def ad_par_layout(self, par, nrow):
        self.grid_layout.addWidget(par.label, nrow, 0)
        self.grid_layout.addWidget(par.curr_val, nrow, 1)
        self.grid_layout.addWidget(par.set_val, nrow, 2)
        self.grid_layout.addWidget(par.set_button, nrow, 3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windowExample = BasicWindow()
    windowExample.show()
    sys.exit(app.exec_())

    
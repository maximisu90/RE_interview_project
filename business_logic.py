from scipy.interpolate import interp1d
import numpy as np
class business_logic():
    
    def __init__(self,parameters=[],clicked_par_key='Beamline energy') :
        self.parameters=parameters
        self.clicked_par_key=clicked_par_key
        data=np.loadtxt('slit_energy_data.txt',skiprows=1)
        self.R=data[:,1]
        self.Exit_slit=data[:,0]
        self.interp_exit_slit=interp1d(self.Exit_slit,1/self.R)
        self.interp_bl_resolution=interp1d(1/self.R,self.Exit_slit)
    def apply_logic_bl_energy(self):
        if (float(self.parameters['Beamline energy'].get_cur_val())>1200)&(self.parameters['Harmonic'].curr_val.text()=='1st'):
            self.parameters['Harmonic'].set_val.setCurrentIndex(1)
            self.parameters['Harmonic'].curr_val.setText('3rd')
        elif (float(self.parameters['Beamline energy'].get_cur_val())<=1200)&(self.parameters['Harmonic'].curr_val.text()=='3rd'):
            self.parameters['Harmonic'].set_val.setCurrentIndex(0)
            self.parameters['Harmonic'].curr_val.setText('1st')

    def apply_logic_exit_slit(self):        
        exit_slit=float(self.parameters['Exit slit'].curr_val.text())
        E=float(self.parameters['Beamline energy'].curr_val.text())
        if exit_slit<=10:
            R=30000
            dE=int(E/R*1e3)
        elif exit_slit>150:
            R=3500
            dE=int(E/R*1e3)
        else:
            dE=round(E*self.interp_exit_slit(exit_slit)*1e3)

        self.parameters["Beamline resolution"].curr_val.setText(f'{dE}')
        self.parameters["Beamline resolution"].set_val.setText(f'{dE}')
        self.apply_logic_combined_resolution()

    def apply_logic_bl_res(self):        
        dE=float(self.parameters["Beamline resolution"].curr_val.text())*1e-3
        E=float(self.parameters['Beamline energy'].curr_val.text())
        R=E/dE
        if R<3500:
            Eslit_interp=150
        elif R>30000:
            Eslit_interp=10
        else:
            Eslit_interp=np.rint(self.interp_bl_resolution(dE/E))
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



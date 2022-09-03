from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
class Parameter_list():
    def __init__(self,name='',current_val='12',value_list=['12','13']):
        font = QFont()
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
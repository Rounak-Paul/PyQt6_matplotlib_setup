from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi

from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )

import numpy as np
import random

from mplwidget import MplWidget

class MatplotlibWidget(QMainWindow):
    
    def __init__(self):
        
        QMainWindow . __init__ ( self )

        loadUi("gui.ui",self)

        self.setWindowTitle("PyQt5 & Matplotlib Setup GUI")

        self.btn = self.findChild(QPushButton,"btn") 
        self.plot_canvas = self.findChild(MplWidget,"plot") 

        self.btn.clicked.connect(self.update_graph)

        self.addToolBar(NavigationToolbar(self.plot_canvas.canvas, self))


    def update_graph(self):

        fs = 500
        f = random.randint(1, 100)
        ts = 1/fs
        length_of_signal = 100
        t = np.linspace(0,1,length_of_signal)
        
        cosine_signal  =  np . cos ( 2 * np . pi * f * t ) 
        sine_signal  =  np . sin ( 2 * np . pi * f * t )

        self.plot_canvas.canvas.axes.clear()
        self.plot_canvas.canvas.axes.plot(t, cosine_signal)
        self.plot_canvas.canvas.axes.plot(t, sine_signal)
        self.plot_canvas.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
        self.plot_canvas.canvas.axes.set_title('Cosinus - Sinus Signal')
        self.plot_canvas.canvas.draw()
        

app = QApplication([])
window = MatplotlibWidget()
window.show()
app.exec_()
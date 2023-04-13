from PyQt6.QtWidgets import*
from  matplotlib.backends.backend_qt5agg  import  FigureCanvas
from  matplotlib.figure  import  Figure
from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar )

class MplWidget(QWidget):
    '''
    TODO
    '''
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)
        self.mplToolBar = NavigationToolbar(self.canvas, self)
        self.layout().addWidget(self.mplToolBar)
        

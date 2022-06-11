from PySide6.QtWidgets import *
from PySide6.QtGui import*
import random
from test import *
w=600
h=600
allbtns=[]
list=[]
xPos=0
yPos=0
light=True
clickCount=0
xCount=0
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.currentWindow=None
        self.resize(w,h)
        for setir in range(3):
            for sutun in range(3):
                btn=Tictacbtn('',Main)
                btn.setGeometry(xPos,yPos,w/3,h/3)
                btn.defineCoordinate(setir,sutun)
                allbtns.append(btn)
                
                xPos+=200
            xPos=0   
            yPos+=200
  
        for btn in allbtns:
                    
            if btn.coord['x']==1:
                if btn.text()=='X':     
                                 
        
                    self.currentWindow=secondWind()
                    self.currentWindow.show() 





class Tictacbtn(QPushButton):
    def __init__(self,*args):
        QPushButton.__init__(self,*args)
        self.clicked.connect(self.clickFunk)
        self.clickCount=0
        
        
        self.coord={
            'x':0,
            'y':0
        }
      
    def clickFunk(self):
        global clickCount
        global light,xCount
        self.clickCount+=1
        print(self.coord)
        if self.clickCount<=1:
            if light:
                self.setText('X')
                self.setStyleSheet('background-color:#79c2d0')
                light=False
            else:
                self.setText('O')
                self.setStyleSheet('background-color:#f70776')
                light=True
    
                                           
        
    def defineCoordinate(self,x,y):
        self.coord['x']=x
        self.coord['y']=y
             






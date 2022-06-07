from PySide6.QtWidgets import *
import random

w=600
h=600


xPos=0
yPos=0

app=QApplication()
main=QMainWindow()
main.resize(w,h)
setirsayi=6
sutunsayi=6
light=True
clickCount=0
class Tictacbtn(QPushButton):
    def __init__(self,*args):
        QPushButton.__init__(self,*args)
        self.clicked.connect(self.clickFunk)
        self.clickCount=0
    def clickFunk(self):
       
        global light
        self.clickCount+=1
        if self.clickCount<=1:
            if light:
                self.setText('X')
                light=False
            else:
                self.setText('O')
                light=true
      
       

for setir in range(3):
    for sutun in range(3):
        btn=Tictacbtn('',main)
        btn.setGeometry(xPos,yPos,w/3,h/3)
        yPos+=200
    yPos=0   
    xPos+=200
main.show()
app.exec_()





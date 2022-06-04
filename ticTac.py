from PySide6.QtWidgets import *
import random

app=QApplication()

main=QMainWindow()
mainWidth=600
mainHeight=600
main.resize(mainWidth,mainHeight)
cellX=0
cellY=0

def btnAction():
    
    button1.setText('x')
    Otext=random.random(button3,button4,button5, button6)   
    print('click') 

def btnAction2():
    
    button2.setText('x')
       
    print('click') 
    
def btnAction3():
    
    button3.setText('x')
       
    print('click')

def btnAction4():
    
    button4.setText('x')
       
    print('click') 

def btnAction5():
    
    button5.setText('x')
       
    print('click') 

def btnAction6():
    
    button6.setText('x')
       
    print('click') 

def btnAction7():
    
    button7.setText('x')
       
    print('click') 
    
def btnAction8():
    
    button8.setText('x')
       
    print('click')    
    
def btnAction9():
    
    button9.setText('x')
       
    print('click')   
    
    

    
button1=QPushButton('',main)
button2=QPushButton('',main)
button3=QPushButton('',main)
button4=QPushButton('',main)
button5=QPushButton('',main)
button6=QPushButton('',main)
button7=QPushButton('',main)
button8=QPushButton('',main)
button9=QPushButton('',main)


button1.clicked.connect(btnAction)
button2.clicked.connect(btnAction2)
button3.clicked.connect(btnAction3)
button4.clicked.connect(btnAction4)
button5.clicked.connect(btnAction5)
button6.clicked.connect(btnAction6)
button7.clicked.connect(btnAction7)
button8.clicked.connect(btnAction8)
button9.clicked.connect(btnAction9)







button1.setGeometry(cellX,cellY,mainWidth/3,mainHeight/3)
button2.setGeometry(0,200,mainWidth/3,mainHeight/3)
button3.setGeometry(0,400,mainWidth/3,mainHeight/3)
button4.setGeometry(200,0,mainWidth/3,mainHeight/3)
button5.setGeometry(200,200,mainWidth/3,mainHeight/3)
button6.setGeometry(200,400,mainWidth/3,mainHeight/3)
button7.setGeometry(400,cellY,mainWidth/3,mainHeight/3)
button8.setGeometry(400,200,mainWidth/3,mainHeight/3)
button9.setGeometry(400,400,mainWidth/3,mainHeight/3)


  
      
    
       
main.show()

app.exec_() 
from operator import truediv
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import random
import keyboard

xPos=300
yPos=300
w=600
h=600
def up():
    global xPos,yPos
    if yPos<h and yPos>0:
        yPos+=5
        snake.setStyleSheet('background:red')
    else:
        snake.setStyleSheet('background:green')

def Foo():
  
    keyboard.read_key()
    while keyboard.read_key()=="w":
        print('dogru')
       
        up()
        
          
  
       

        
app=QApplication()

game=QMainWindow()

game.resize(w,h)

snake=QPushButton('',game)
snake.setGeometry(xPos,yPos,50,50)
snake.clicked.connect(Foo)



game.show()
app.exec_()
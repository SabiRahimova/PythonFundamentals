from operator import truediv
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import random

# while True:
#     keyboard.read_key()
#     # if keyboard.read_key()=="up":
#     #     Up()
#     # elif keyboard.read_key()=="down":
#     #     Down()
#     # elif keyboard.read_key()=="left":
#     #     Left()
#     # elif keyboard.read_key()=="right":
#     #     Right()
#     # else:
#     #     break

score=0
xPos=300
yPos=300
snakeWidth=50
snakeHeight=50

mxPos=random.randint(50,750)
myPos=random.randint(50,750)

def Up():
    global yPos,xPos,mxPos,myPos,score,snakeWidth,snakeHeight
    yPos-=50
    snake.move(xPos,yPos)
    if CheckX() and CheckY():
        score+=1
        snakeHeight+=50
        snake.resize(snakeWidth,snakeHeight)
        snake.setText(str(score))
        mxPos=random.randint(50,750)
        myPos=random.randint(50,750)
        meal.setGeometry(mxPos,myPos,50,50)
        meal.setStyleSheet('background:transparent')
        
        
    else:
        meal.setStyleSheet('background:red')

def Down():
    global yPos,xPos,mxPos,myPos,score,snakeHeight
    yPos+=50
    snake.move(xPos,yPos)
    if CheckX() and CheckY():
        score+=1
        snakeHeight+=50
        snake.resize(snakeWidth,snakeHeight)
        
        snake.setText(str(score))
        mxPos=random.randint(50,750)
        myPos=random.randint(50,750)
        meal.setGeometry(mxPos,myPos,50,50)
        meal.setStyleSheet('background:green')
         
    else:
        meal.setStyleSheet('background:red')  

def Left():
    global yPos,xPos,mxPos,myPos,score,snakeWidth
    xPos-=50
    snake.move(xPos,yPos)
    if CheckX() and CheckY():
        score+=1
        snakeWidth+=50
        snake.resize(snakeWidth,snakeHeight)
        snake.setText(str(score))
        mxPos=random.randint(50,750)
        myPos=random.randint(50,750)
        meal.setGeometry(mxPos,myPos,50,50)
        meal.setStyleSheet('background:green')
        
        print('deydi')
    else:
        meal.setStyleSheet('background:red')
        print('deymedi')

def Right():
    global yPos,xPos,mxPos,myPos,score,snakeWidth
    xPos+=50
    snake.move(xPos,yPos)
    if CheckX() and CheckY():
        score+=1
        snakeWidth+=50
        snake.resize(snakeWidth,snakeHeight)
        snake.setText(str(score))
        mxPos=random.randint(50,750)
        myPos=random.randint(50,750)
        meal.setGeometry(mxPos,myPos,50,50)
        
def CheckX():
    print(xPos,mxPos,yPos,myPos)
    if xPos>mxPos-50 and xPos<mxPos+50:
        return True
    else:
        return False     
def CheckY():
    print(xPos,mxPos,yPos,myPos)
    if yPos>myPos-50 and yPos<myPos+50:
        
        return True
    else:
        return False  
app=QApplication()

game=QMainWindow()

game.resize(800,800)

snake=QPushButton('',game)
snake.setGeometry(300,300,50,50)

meal=QPushButton('',game)
meal.setGeometry(mxPos,myPos,50,50)
meal.setStyleSheet('background:red')
up=QPushButton('Up',game)
up.clicked.connect(Up)
up.setGeometry(10,10,100,30)
down=QPushButton('Down',game)
down.clicked.connect(Down)
down.setGeometry(120,10,100,30)
left=QPushButton('Left',game)
left.clicked.connect(Left)
left.setGeometry(230,10,100,30)
right=QPushButton('Right',game)
right.clicked.connect(Right)
right.setGeometry(340,10,100,30)
game.show()
app.exec_()
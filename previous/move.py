from PySide6.QtWidgets import*



def up():
    yPos=385
    if yPos>0:
        while True:
            xPos=385
            yPos=385
            yPos=yPos-20
            ball.move(xPos,yPos)
        
      
xPos=385
yPos=385  
def down():
    
    global xPos,yPos
    yPos+=20
    ball.move(xPos,yPos)
        
def left():
    global xPos,yPos
    xPos-=20
    ball.move(xPos,yPos)

def right():
    global xPos,yPos
    xPos+=20
    ball.move(xPos,yPos)
    





app=QApplication()

gamewindow=QWidget()
gamewindow.resize(800,800)


ball=QPushButton(" ",gamewindow)
ball.resize(40,40)
ball.setStyleSheet("background:red")
ball.move(385,385)
upbtn=QPushButton("go up",gamewindow)
upbtn.setGeometry(10,10,120,30)
upbtn.clicked.connect(up)
downbtn=QPushButton("go down",gamewindow)
downbtn.setGeometry(120,10,120,30)
downbtn.clicked.connect(down)
leftbtn=QPushButton("go left",gamewindow)
leftbtn.setGeometry(220,10,120,30)
leftbtn.clicked.connect(left)
rightbtn=QPushButton("go right",gamewindow)
rightbtn.setGeometry(360,10,120,30)
rightbtn.clicked.connect(right)

gamewindow.show()
app.exec_()


    
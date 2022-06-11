from PySide6.QtWidgets import *


w=400
h=300



Main=QWidget()
Main.resize(w,h)
Main.setStyleSheet('background-color:#f8f398')

title=QLabel(" Congratulations! You Won /n Do you want to play again?",Main)
title.setGeometry(40,50,400,30)
title.setStyleSheet('font-size:23px; ')

YesBtn=QPushButton('Yes',Main)
YesBtn.setGeometry(30,130,150,70)
YesBtn.setStyleSheet('background-color:#c50000; font-size:20px; ')
NoBtn=QPushButton('No',Main)
NoBtn.setGeometry(220,130,150,70)
NoBtn.setStyleSheet('background-color:green ;font-size:20px;')






    
            
Main.show()


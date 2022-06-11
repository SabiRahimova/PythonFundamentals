from PySide6.QtWidgets import *
import random

app=QApplication()

main=QMainWindow()
mainWidth=600
mainHeight=600
main.resize(600,800)
cellX=0
cellY=0
btnList=[]
clickCount=0
light=True
def btnAction():
    btnList.append(button1)
    button1.setText('X')
    button1.setEnabled(False)
    list.remove(button1)
    i=random.choice(list)
    
    
    if i!=button1 and i!=i.setEnabled(False):
        i.setText('O')
        i.setEnabled(False)
        list.remove(i)
            
    if i==button1 or i==i.setEnabled(False):
        i=random.choice(list)
        if i!=button1 and i!=i.setEnabled(False):
            i.setText('O')
            i.setEnabled(False)
            list.remove(i)  
                
     
    print(list) 

def btnAction2():
    btnList.append(button2)
    button2.setText('X')
    button2.setEnabled(False)
    list.remove(button2)
    i=random.choice(list)
    if i!=button2 and i!=i.setEnabled(False):
        i.setText('O')
        i.setEnabled(False)
        list.remove(i)
       
    if i==button2 or i==i.setEnabled(False):
        i=random.choice(list)       
        if i!=button2 and i!=i.setEnabled(False):
            i.setText('O')
            i.setEnabled(False)
            list.remove(i)
           
    print(list) 
    
def btnAction3():
    btnList.append(button3)
    button3.setText('X')
    button3.setEnabled(False)
    list.remove(button3)
    i=random.choice(list)
    
            
    if i==button3 or i==i.setEnabled(False):
        i=random.choice(list)
        if i!=button3 and i!=i.setEnabled(False):
            i.setText('O')
            i.setEnabled(False)
            list.remove(i)  
             
    if i!=button3 and i!=i.setEnabled(False):
        i.setText('O')
        i.setEnabled(False)
        list.remove(i)
          
    print('click')

def btnAction4():
    btnList.append(button4)
    button4.setText('X')
    button4.setEnabled(False)
    list.remove(button4)
    i=random.choice(list)
    if i!=button4 and i!=i.setEnabled(False):
        i.setText('O')
        i.setEnabled(False)
        list.remove(i)
    if i==button4  or i==i.setEnabled(False):
        i=random.choice(list)  
        if i!=button4 and i!=i.setEnabled(False):
            i.setText('O')
            i.setEnabled(False)
            list.remove(i)
            
       
    print('click') 

def btnAction5():
    btnList.append(button5)
    button5.setText('X')
    button5.setEnabled(False)
    list.remove(button5)
    i=random.choice(list)
    if i!=button5 and i!=i.setEnabled(False):
        i.setText('O')
        i.setEnabled(False)
        list.remove(i)
    if i==button5 or i==i.setEnabled(False):
        i=random.choice(list)  
        if i!=button5 and i!=i.setEnabled(False):
            i.setText('O')
            i.setEnabled(False)
            list.remove(i)
         
    print('click') 

def btnAction6():
    btnList.append(button6)
    button6.setText('X')
    button6.setEnabled(False)
    list.remove(button6)
    i=random.choice(list)
    if i!=button6 and i!=i.setEnabled(False):
        i.setText('O')
        i.setEnabled(False)
        list.remove(i)
    if i==button6 or i==i.setEnabled(False):
        i=random.choice(list)  
        if i!=button6 and i!=i.setEnabled(False):
            i.setText('O')
            i.setEnabled(False)
            list.remove(i)
    print('click') 

def btnAction7():
    btnList.append(button7)
    button7.setText('X')
    button7.setEnabled(False)
    list.remove(button7)
    i=random.choice(list)
    if i!=button7 and i!=i.setEnabled(False):
        i.setText('O')
        i.setEnabled(False)
        list.remove(i)
        
    if i==button7 or i==i.setEnabled(False):
        i=random.choice(list)  
        if i!=button7 and i!=i.setEnabled(False):
            i.setText('O')
            i.setEnabled(False)
            list.remove(i)
         
        
      
    print('click') 
    
def btnAction8():
    btnList.append(button8)
    button8.setText('X')
    button8.setEnabled(False)
    list.remove(button8)
    i=random.choice(list)
    if i!=button8 and i!=i.setEnabled(False):
        i.setText('O')
        i.setEnabled(False)
        list.remove(i)
       
    if i==button8 or i==i.setEnabled(False):
            i=random.choice(list)  
            if i!=button8 and i!=i.setEnabled(False):
                i.setText('O')
                i.setEnabled(False)
                list.remove(i)
          
    print('click')    
    
def btnAction9():
    btnList.append(button9)
    button9.setText('x')
    button9.setEnabled(False)
    list.remove(button9)
    i=random.choice(list)
    if i!=button9 and i!=i.setEnabled(False):
        i.setText('O')
        i.setEnabled(False)
        list.remove(i)
        
    if i==button9 or i==i.setEnabled(False):
        i=random.choice(list)  
            
        if i!=button9 and i!=i.setEnabled(False):
            i.setText('O')
            i.setEnabled(False)
            list.remove(i)
             
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

#if 'button1' and 'button2' and 'button3' in btnList:
    #print('Yes,X won')   
 
#if 'button1' and 'button4' and 'button7' in btnList:
    #print('YES, X won')    
 
#if 'button2' and 'button5' and 'button8' in btnList:
    #print('Yes,X won')   
 
#if 'button3' and 'button6' and 'button9' in btnList:
    #print('Yes,X won')   

#if 'button4' and 'button5' and 'button6' in btnList:
    #print('Yes,X won')   
 
#if 'button7' and 'button8' and 'button9' in btnList:
    #print('Yes,X won')   
 
#if 'button1' and 'button5' and 'button9' in btnList:
    #print('Yes,X won')   

#if 'button3' and 'button5' and 'button7' in btnList:
    #print('Yes,X won')       
       


button1.clicked.connect(btnAction)
button2.clicked.connect(btnAction2)
button3.clicked.connect(btnAction3)
button4.clicked.connect(btnAction4)
button5.clicked.connect(btnAction5)
button6.clicked.connect(btnAction6)
button7.clicked.connect(btnAction7)
button8.clicked.connect(btnAction8)
button9.clicked.connect(btnAction9)


cord123=[button1,button2,button3]
cord147=[button1,button4,button7]
cord258=[button2,button5,button8]
cord369=[button3,button6,button9]
cord456=[button4,button5,button6]
cord789=[button7,button8,button9]
cord159=[button1,button9,button9]
cord357=[button3,button5,button9]

check=all(items in btnList for items in cord123)
if check is True:
    print('Yes,x won')

check=all(items in btnList for items in cord147)
if check is True:
    print('Yes,x won')

check=all(items in btnList for items in cord258)
if check is True:
    print('Yes,x won')
    
check=all(item in btnList for item in cord369)
if check is True:
    print('Yes,x won')   

check=all(items in btnList for items in cord456)
if check is True:
    print('Yes,x won')    

check=all(items in btnList for items in cord789)
if check is True:
    print('Yes,x won')   
    
check=all(items in btnList for items in cord159)
if check is True:
    print('Yes,x won') 
    
check=all(items in btnList for items in cord357)
if check is True:
    print('Yes,x won') 
button1.setGeometry(cellX,cellY,mainWidth/3,mainHeight/3)
button2.setGeometry(0,200,mainWidth/3,mainHeight/3)
button3.setGeometry(0,400,mainWidth/3,mainHeight/3)
button4.setGeometry(200,0,mainWidth/3,mainHeight/3)
button5.setGeometry(200,200,mainWidth/3,mainHeight/3)
button6.setGeometry(200,400,mainWidth/3,mainHeight/3)
button7.setGeometry(400,cellY,mainWidth/3,mainHeight/3)
button8.setGeometry(400,200,mainWidth/3,mainHeight/3)
button9.setGeometry(400,400,mainWidth/3,mainHeight/3)


list=[ button1,button2, button3,button4,button5,button6,button7,button8,button9]

main.show()

app.exec_() 
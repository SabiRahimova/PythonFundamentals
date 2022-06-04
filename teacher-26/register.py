from PySide6.QtWidgets import *
from data import users,User
qroups=["Modul01","Modul02","Modul03","Modul04"]
class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('App - Register Window')
        self.resize(220,400)
        self.title=QLabel("Register New User",self)
        self.title.setGeometry(10,10,200,30)
        self.nameText=QLineEdit("Ad",self)
        self.nameText.setGeometry(10,50,200,30)
        self.surnameText=QLineEdit("Soyad",self)
        self.surnameText.setGeometry(10,90,200,30)
        self.qroup=QComboBox(self)
        self.qroup.addItems(qroups)
        self.qroup.setGeometry(10,130,200,30)
        self.regBtn=QPushButton("Add",self)
        self.regBtn.setGeometry(10,170,200,30)
        self.regBtn.clicked.connect(self.registerUser)

    def registerUser(self):
       user=User(self.nameText.text(),self.surnameText.text(),self.qroup.currentText())
       users.append(user)
       print(self.qroup.currentText())
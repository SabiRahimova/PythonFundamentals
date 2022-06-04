from PySide6.QtWidgets import *
from data import users
class DataTable(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,360)
        self.setWindowTitle('App - Users')
        self.showBtn=QPushButton('Show Users',self)
        self.showBtn.setGeometry(10,10,200,30)
        self.showBtn.clicked.connect(self.showUsers)
        self.resultText=QTextBrowser(self)
        self.resultText.setGeometry(10,50,480,300)
    def showUsers(self):
        txt=""
        for user in users:
            txt+=f'{user.Ad},{user.Soyad},{user.Qrup}\n'
        self.resultText.setText(txt)
        print(users)
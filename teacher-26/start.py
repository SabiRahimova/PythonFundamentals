from PySide6.QtWidgets import *
from register import Register
from datatable import DataTable
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.currentWindow=None
        self.resize(600,600)
        self.setWindowTitle("App-Welcome")
        self.registerBtn=QPushButton('Register',self)
        self.registerBtn.resize(200,30)
        self.registerBtn.move(10,10)
        self.registerBtn.clicked.connect(self.openRegisterWindow)
        self.loginBtn=QPushButton('Login',self)
        self.loginBtn.resize(200,30)
        self.loginBtn.move(230,10)
        self.loginBtn.clicked.connect(self.openLoginWindow)
    def openRegisterWindow(self):
        self.currentWindow=Register()
        self.currentWindow.show()

    def openLoginWindow(self):
        self.currentWindow=DataTable()
        self.currentWindow.show()
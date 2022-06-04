from PySide6.QtWidgets import QApplication,QWidget,QMainWindow,QLabel,QLineEdit,QPushButton
def topla():
    a=int(atext.text())
    b=int(btext.text())
    netice.setText(f'netice:{a+b}')

app=QApplication()
main=QMainWindow()
main.resize(500,500)
main.setWindowTitle('sabi')
atext=QLineEdit("a ededi: ",main)
atext.setGeometry(10,10,250,40)
btext=QLineEdit("b ededi: ",main)
btext.setGeometry(10,50,250,40)
hesabla=QPushButton('topla',main)
hesabla.setGeometry(10,90,250,40)
hesabla.clicked.connect(topla)

netice=QLabel("netice",main)
netice.setGeometry(10,140,250,40)


main.show()
app.exec_()
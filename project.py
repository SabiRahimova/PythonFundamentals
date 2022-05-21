from tkinter import *
root=Tk()
root.geometry('508x300')

projectMenu= """
            Welcome to Menu:
            
    `````````````````````````````````````
        1.Add a new user
        2.Show user information.
        3.Set user information for the current database.
        4.Delete user account.
        
    ``````````````````````````````````````
    """    
    
print(projectMenu)
UserList=[]

def newUser():
    A_New_User="""
````````New_User_Registration ````````````
    
    """
    print(A_New_User)
    
    Id=input('Enter ID please: ')
    Name=input('Enter Name please: ')
    Suername=input('Enter Surname please:')
    Password=input('Enter password please: ')
    


def showUser():
    userinfo="""
    ```````User_Information``````
    """
    print(userinfo)
    

def setInfo():
    set_info="""
    ```````Set user information for the current database``````
    """
    print(set_info)
    
    
def DeleteAccount():
    delete_User="""  
    ````````` Delete_user_account````````
    """
    print(delete_User)
    

while True:
    UserList.append(input())
    
    choise=input('Enter the command: ')
    
    if choise=="1":
        newUser()
    
    elif choise=="2":
        showUser() 
    
    elif choise=="3":
        setInfo()
    
    elif choise=="4":
        DeleteAccount()
    
    else:
        print( "The command is not correct, please try your command again" )
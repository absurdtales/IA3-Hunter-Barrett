from APIrequest import API
from Parse import parsing
from UserLogin import User
cParse = parsing()
cUser = User()
cParse.parse()
access = False
while access == False:
    result = input("Would you like to login or Register ")
    if (result).lower() == "register":
        cUser.register()
        access = True
    elif (result).lower() == "login":
        A=cUser.login()
        access = A
        A = True
        if A == False:
            print("Successful Login")
        else:
            print("Successful Login")
    else:
        pass


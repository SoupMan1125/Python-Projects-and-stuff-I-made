import os, time
while True:
    print(" ===== LOGIN OR SIGNUP =====")
    print("1 : Signup")
    signup = input(": ")
    if signup ==  "1":
        os.system("cls")
        userUser = input("Choose a username! : ")
        userPass = input("Choose a good password! : ")
        print("")
        print(" ===== Succses! ===== ")
        time.sleep(2)
        os.system("cls")
        break
    else:
        os.system("cls")
        print("INVALID INPUT, please try again.")
        time.sleep(3)
        os.system("cls")
while True:
    print(" ===== LOGIN =====")
    print(" 1 : Login")
    login = int(input(": "))
    if login == 1:
        while True:
            os.system("cls")
            loginUser = input("Enter Username : ")
            loginPass = input("Enter Passowrd : ")
            if loginUser == userUser and loginPass == userPass:
                os.system("cls")
                print(" ===== LOGIN SUCCSES WELLCOM TOO ____ =====")
                time.sleep(5)
                exit()
            else:
                os.system("cls")
                print(" ===== ERROR : USERNAME OR PASSOWRD NOT VALID, please try again. ===== ")
                time.sleep(5)
    else:
        os.system("cls")
        print("INVALID INPUT, please try again.")
        time.sleep(3)
        os.system("cls")
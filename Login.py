from time import sleep
import os


def checkAccount():
    with open("Files\\Usernames.txt", "r") as Users, open("Files\\LoggedIn.txt", "r") as islogged:
        Users.seek(0)
        islogged.seek(0)

        usernames = Users.read().strip()
        logstatus = islogged.read().strip()
        if usernames and logstatus == "True":
            return True
        elif usernames and logstatus == "False":
            return False
        else:
            return None


def Login():
    signIn = input("Do you want to log in your account? [y/n] ")
    if signIn == "y":
        print("Loading...")
        sleep(1)
        loginStatus = checkAccount()
        if loginStatus == None:
            signUp = input(
                "You don't have an account! Do you want to create one? [y/n] ")
            if signUp == "y":
                os.startfile("CreateAccount.py")
                exit()
            elif signUp == "n":
                print("Ok! Exiting...")
                sleep(1.5)
                exit()
            else:
                return Login()
        elif loginStatus == True:
            logOut = input(
                "You are already logged in! Do you want to log out? [y/n] ")
            if logOut == "y":
                print("Ok! Logging you out...")
                with open("Files\\LoggedIn.txt", "w") as Log:
                    Log.write("False")
                sleep(2)
                print("Logged out! Exiting...")
                sleep(1.5)
                exit()
            elif logOut == "n":
                print("Ok! Exiting...")
                sleep(1.5)
                exit()
            else:
                return Login()
        else:
            pass
        sleep(2)
        print("Loaded!")
    elif signIn == "n":
        print("Ok! Exiting...")
        sleep(1.5)
        exit()
    else:
        return Login()


def inputUser():
    username = input("Username: ")
    with open("Files\\Usernames.txt") as names:
        name = names.read().strip()
        if username != name:
            print("Wrong username!")
            return inputUser()


def inputPassword():
    password = input("Password: ")
    with open("Files\\Passwords.txt") as passwords:
        passw = passwords.read().strip()
        if password == passw:
            print("Logging you in...")
            sleep(1)
            with open("Files\\LoggedIn.txt", "w") as doLogin:
                doLogin.write("True")
                sleep(1)
                print("Logged in! Exiting...")
                sleep(1.5)
                exit()
        else:
            print("Wrong password!")
            return inputPassword()


Login()
inputUser()
inputPassword()

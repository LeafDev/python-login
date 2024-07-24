from time import sleep
from os import startfile


def checkAccount():
    with open("Files\\Usernames.txt", "r") as check:
        for checkOk in check:
            if checkOk:
                existsAccount = input(
                    "You already have an account! Did you forget the password? [y/n] ")
                if existsAccount == "y":
                    with open("Files\\Passwords.txt", "r+") as passwordsFile:
                        for passwords in passwordsFile:
                            print(f"Your password is {passwords} ")
                            sleep(3)
                            print("Exiting...")
                            sleep(1.5)
                            exit()

                elif existsAccount == "n":
                    print("Ok! Exiting...")
                    sleep(0.5)
                    exit()
                else:
                    return checkAccount()


def askCreate():
    wantsToLogin = input("Do you want to create an account? [y/n] ")
    if wantsToLogin == "y":
        print("Loading account creation...")
        sleep(1)
        checkAccount()
        sleep(2.5)
        print("Loaded!")
    elif wantsToLogin == "n":
        print("Okay, come back whenever you want.")
        sleep(1.5)
        exit()
    else:
        return askCreate()


def createUser():
    name = input("What's your username? ")
    if name == "" or name == " ":
        print("Please, at least one character.")
        return createUser()
    else:
        with open("Files\\Usernames.txt", "w") as usernamesFile:
            usernamesFile.write(name)
            usernamesFile.seek(0)


def createPass():
    password = input("What's your password? ")
    if password == "" or password == " ":
        print("Please, at least one character.")
        return createPass()
    else:
        with open("Files\\Passwords.txt", "w") as passwordsFile:
            passwordsFile.write(password)
            passwordsFile.seek(0)


askCreate()
createUser()
createPass()
print("Creating your account...")

sleep(1.5)

print("Account created sucessfully!")


def login():
    askLogin = input("Do you want to log in your account now? [y/n] ")

    if askLogin == "y":
        print("Ok! Lauching Login.py...")
        sleep(2)
        startfile("Login.py")
        exit()
    elif askLogin == "n":
        print("Ok! Exiting...")
        sleep(1.5)
        exit()
    else:
        return login()


login()

from time import sleep
from os import startfile


def deleteAccount():
    with open("Files\\Usernames.txt", "r+") as Users:
        Usernames = Users.read().strip()
        if not Usernames:
            askCreateAcc = input(
                "You don't have an account! Do you want to create a new one? [y/n] ")
            if askCreateAcc == "y":
                print("Ok! Lauching CreateAccount.py...")
                sleep(2)
                startfile("CreateAccount.py")
                exit()
            elif askCreateAcc == "n":
                print("Ok! Exiting...")
                sleep(1.5)
                exit()
            else:
                return deleteAccount()
        else:
            askDel = input(
                "Are you sure you want to delete your account? [y/n] ")
            if askDel == "y":
                with open("Files\\Passwords.txt", "w") as Passwords, open("Files\\LoggedIn.txt", "w") as isLogged:
                    print("Ok! Deleting...")
                    sleep(1)
                    Users.seek(0)
                    Users.write("")
                    Users.truncate()
                    Passwords.write("")
                    isLogged.write("False")
                    sleep(1)
                    print("Account deleted! Exiting...")
                    sleep(1.5)
                    exit()
            elif askDel == "n":
                print("Ok! Exiting...")
                sleep(1.5)
                exit()
            else:
                return deleteAccount()


deleteAccount()

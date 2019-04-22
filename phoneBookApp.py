#================================#
## Phone Book App Exercises ##


def lookupFunc():
    lookup = input("What name are you looking for?").capitalize()
    if lookup in myPhonebook:
        print(f"Found entry for {lookup}:", myPhonebook.get(f"{lookup}")["Phone Number: "])
        input("Continue >>>")
    else:
        print("That name does not exist...")
        input("Continue >>>")

def addNameFunc():
    name = input("What is the name?").capitalize()
    myPhonebook[f"{name}"] = {}
    number = input("What is the phone number?")
    myPhonebook[f"{name}"]["Phone Number: "] = f"{number}"
    print(f"Entry stored for {name}.")
    input("Continue >>>")

def delNameFunc():
    delete = input("What name would you like to delete?").capitalize()
    if delete in myPhonebook:
        del myPhonebook[delete]
        print(f"Deleted entry for {delete}")
        input("Continue >>>")
    else:
        print("That name does not exist...")
        input("Continue >>>")

def listNameFunc():
    for names in myPhonebook:
        print(f"Found entry for {names}:", myPhonebook.get(f"{names}")["Phone Number: "])
    input("Continue >>>")


def quitFunc():
    print("Bye!")


myPhonebook = {}
def init():
    while True:
        print("")
        print("======================")
        print("Electronic Phone Book")
        print("======================")
        print("1.  Look up an entry")
        print("2.  Set an entry")
        print("3.  Delete an entry")
        print("4.  List all entries")
        print("5.  Quit")
        print("")
        entry = int(input("What do you want to do? (1-5) "))
        if entry == 1:
            lookupFunc()
        if entry == 2:
            addNameFunc()
        if entry == 3:
            delNameFunc()
        if entry == 4:
            listNameFunc()
        elif entry >= 5:
            quitFunc()
            break

init()
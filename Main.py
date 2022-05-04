from pprint import pprint


credentialFile = open("credentialsfile.txt", 'r')
inputFile = credentialFile.readlines()

fileCheck = "griffin.kees"
numAttempts = 3


def validateUserName(userName):
    global numAttempts
    isFound = False
    for line in inputFile:
        if userName in line:
            isFound = True
            break
    return isFound


def validatePassword(userPassword):
    if userPassword == "password":
        print("Correct")


def consumeAttempt():
    global numAttempts
    numAttempts -= 1
    print("Username does not exist, please try again, you have {} attempts remaining".format(numAttempts))


def exitClient():
    print("Exiting client")
    quit()


while (numAttempts > 0):
    userName = input("Enter User Name or Q to exit: ")
    if userName == "Q" or userName == "q":
        exitClient()
    else:
        if validateUserName(userName):
            userPassword = input("Enter password: ")
            validatePassword(userPassword)
        else:
            consumeAttempt()

print("Too many failed attempts, exiting")

from pprint import pprint
import json
import getpass


from UserInfo import userInfo

credentialFile = "userCredentials.json"
numAttempts = 3

# Function to track and display attempt information


def checkNumAttempts():
    if numAttempts > 0:
        print("{} attempts remaining".format(numAttempts))
    else:
        print("Exceeded maximum number of attempts, system will now exit")
        exitClient()

# Simple function to exit with message.


def exitClient():
    print("Exiting client")
    quit()


print("Please enter a selection")
print("1. Login")
print("2. Exit")
userSelection = input("")
if userSelection == "1":
    # Attempts this loop while there are still attempts remaining.
    while numAttempts > 0:
        userName = input("Enter User Name: ")
        # create new instance of getpass in order to conceal password input echoing.
        userPassword = getpass.getpass("Enter password: ")
        # Creates new instance of UserInfo class passing the username, password, and default credential file as arguments
        validatedSystemUser = userInfo(
            userName, userPassword, credentialFile)
        # Checks the return of the validateUser function, and if true displays role file, otherwise reduces
        # the number of attempts and re enters the loop for an additional attempt.
        if validatedSystemUser.validateUser():
            validatedSystemUser.displayRoleFile()
            break
        else:
            numAttempts -= 1
            checkNumAttempts()
else:
    exitClient()

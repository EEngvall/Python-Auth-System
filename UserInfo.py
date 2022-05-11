from pprint import pprint
import json
import hashlib
from os.path import exists


class userInfo:
    userRole = ""
    userCredentialStr = ""
    hashedPassword = ""
    salt = "x455L0"
    isExistingUser = False

    def __init__(self, userName, userPassword, credentialFile):
        self.userName = userName
        self.userPassword = userPassword
        self.credentialFile = credentialFile
        # Apply MD5 hash to user input for password value.
        result = hashlib.md5((self.userPassword + self.salt).encode())
        self.hashedPassword = result.hexdigest()

    def getUserName(self):
        return self.userName

    def getUserPassword(self):
        return self.userPassword

    def getUserRole(self):
        return self.userRole

    def setUserRole(self, role):
        self.userRole = role

    def setUserCredentialStr(self, credentialStr):
        self.userCredentialStr = credentialStr

    # Validates uername and password against JSON contents
    def validateUser(self):
        userValidated = False
        with open(self.credentialFile, 'r') as dataFile:
            data = json.load(dataFile)
            # Iterate through the JSON file searching for the matching Key:Values
            for key in data["credentials"]:
                if self.userName == key["username"]:
                    # print(self.hashedPassword)
                    if self.hashedPassword == key["passwordHash"]:
                        userValidated = True
                        self.userRole = key["role"]
                    else:
                        print("Incorrect Password")
        return userValidated

    # Cross checks existing usernames in the JSON file to prevent duplicate usernames from being added.
    def checkUsernameAvailability(self):
        userNameAvailable = True
        with open(self.credentialFile, 'r') as dataFile:
            data = json.load(dataFile)
            # Iterate through the JSON file searching for the matching Key:Values
            for key in data["credentials"]:
                if self.userName == key["username"]:
                    userNameAvailable = False

        return userNameAvailable

    # Creates a new user based on input collected and appends the JSON file with these values.
    def createNewUser(self):
        new_data = {"username": self.userName, "password": self.userPassword,
                    "role": self.userRole, "passwordHash": self.hashedPassword}

        if self.checkUsernameAvailability():
            with open(self.credentialFile, 'r+') as file:
                # First we load existing data into a dict.
                file_data = json.load(file)
                # Join new_data with file_data inside emp_details
                file_data["credentials"].append(new_data)
                # Sets file's current position at offset.
                file.seek(0)
                # convert back to json.
                json.dump(file_data, file, indent=4)
                print("You've successfully registered a new account!")
                self.isExistingUser = True
        else:
            print("Username already exists")
            self.isExistingUser = False
        return self.isExistingUser

    # Prints contents of user role file to screen
    def displayRoleFile(self):
        if exists(self.userRole + ".txt"):
            print()
            with open(self.userRole + ".txt", "r") as file:
                for line in file:
                    print(line)
            print()
        else:
            print("No role file exists for selected role")

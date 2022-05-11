from pprint import pprint
import json
import hashlib


class userInfo:
    userRole = ""
    userCredentialStr = ""
    hashedPassword = ""

    def __init__(self, userName, userPassword, credentialFile):
        self.userName = userName
        self.userPassword = userPassword
        self.credentialFile = credentialFile

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

    def createPasswordHash(self):
        result = hashlib.md5(self.userPassword.encode())
        self.hashedPassword = result.hexdigest()

    def validateUser(self):
        userValidated = False
        with open(self.credentialFile, 'r') as dataFile:
            data = json.load(dataFile)
            # Iterate through the JSON file searching for the matching Key:Values
            for key in data["credentials"]:
                if self.userName == key["username"]:
                    # Apply MD5 hash to user input for password value.
                    self.createPasswordHash()
                    print(self.hashedPassword)
                    if self.hashedPassword == key["passwordHash"]:
                        userValidated = True
                        self.userRole = key["role"]
                    else:
                        print("Incorrect Password")
        return userValidated
        # print(key["username"])

    # Prints contents of user role file to screen
    def displayRoleFile(self):
        print()
        with open(self.userRole + ".txt", "r") as file:
            for line in file:
                print(line)
        print()

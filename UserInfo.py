from pprint import pprint


class userInfo:

    userRole = ""
    userCredentialStr = ""

    def getUserRole(self):
        return self.userRole

    def setUserRole(self, role):
        self.userRole = role

    def getUserCredentialStr(self):
        return self.userCredentialStr

    def setUserCredentialStr(self, credentialStr):
        self.userCredentialStr = credentialStr

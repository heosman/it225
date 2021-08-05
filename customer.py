class Customer():
    def __init__(self, userid, phonenumber):
        self.userid=userid
        self.phonenumber=phonenumber

    def getUserID(self):
        return self.userid

    def getPhoneNumber(self):
        return self.phonenumber

    def __str__(self):
        return self.userid + ' ' + self.phonenumber
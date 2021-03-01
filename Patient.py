class Patient:

    def __init__(self, name, contact,email,loc,time, query="COVID"):
        self.__day = time
        self.__name = name
        self.__mail = email
        self.__contactNumber = contact
        self.__depart = query
        self.location = loc

    def getName(self):
        return self.__name

    def getTime(self):
        return self.__day

    def getContact(self):
        return self.__contactNumber

    def getDepart(self):
        return self.__depart

    def getEmail(self):
        return self.__mail

    def getLocation(self):
        return self.location



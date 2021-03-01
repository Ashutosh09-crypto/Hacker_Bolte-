
class Doctor:

    def __init__(self,name,contact,depart, hospi,avaibility = "Mon to Fri\nFrom 9am to 2pm."):
        self.__name = name
        self.__contactNumber = contact
        self.__depart = depart
        self.__available = avaibility
        self.__hospital = hospi

    def getName(self):
        return self.__name

    def getContact(self):
        return self.__contactNumber

    def getDepart(self):
        return self.__depart

    def getAvailable(self):
        return self.__available

    def getHospital(self):
        return self.__hospital

    def setName(self,n):
        self.__name = n

    def setContact(self,c):
        self.__contactNumber = c

    def setDepart(self,d):
        self.__depart = d

    def changeAvalible(self,time):
        self.__available = time

    def changeHospi(self,hospi):
        self.__hospital = hospi
from Doctor import Doctor
import smtplib

class Hospital:

    peoplesRated = 0

    def __init__(self, nam, loc, doctorList,contact, rate="No reviews yet\n"):
        self.__HelpLine = contact
        self.__doctors = self.__makeDoctorsList(doctorList)
        self.__name = nam
        self.__location = loc
        self.__rating = rate
        self.__doctFile = doctorList
        self.__patientList = open("{}patientlist.txt".format(nam),'w+')
        self.__patientList.close()



    def rateMe(self,ratings):
        # self.__rating = ((self.__rating * (self.peoplesRated-1)) + ratings)/self.peoplesRated
        return ratings

    def getHelpLine(self):
        return self.__HelpLine

    def getLocation(self):
        return self.__location

    def getName(self):
        return self.__name

    def displayDoctors(self):
        for doctors in self.__doctors:
            doctor = self.__doctors[doctors]
            return (doctor.getName(),doctor.getContact(),doctor.getDepart(),doctor.getAvailable())

    def patients(self):
        return self.__patientList


    def __makeDoctorsList(self,file):
        docList = {}
        with open(file, 'r') as docF:
            data = docF.readlines()
            for x in range(0, len(data)):
                line = data[x]
                infos = line.split(",")
                name = infos[0].strip()
                contact = infos[1].strip()
                depart = infos[2].strip()
                avail = infos[3].strip()
                # print(name,contact,depart,avail)
                doctor = Doctor(name,contact,depart,self,avail)
                docList[name] = doctor

        return docList


    def setReminder(self,idAddress,sub,time,doctor,name):

        # set reminder for subject on date to emailAddress
        smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_object.ehlo()
        smtp_object.starttls()
        email = "zenbot2020covid@gmail.com"
        password = "acszxkxrjqngwclb"
        smtp_object.login(email, password)

        from_address = email
        to_address = idAddress
        subject = sub
        message = "Hello {},\n\t Your apointment is fixed on date {} with {}.\nThanks\n{}".format(name,time,doctor,self.__name)
        msg = "Subject: " + subject + '\n' + message
        smtp_object.sendmail(from_address, to_address, msg)
        print(to_address)

    def entryPatient(self,patient,doctor):
        f = open("{}patientlist.txt".format(self.__name),'a+')

        name = patient.getName()
        loc = patient.getLocation()
        id = patient.getEmail()
        query = patient.getDepart()
        day = patient.getTime()

        f.write("{}, {}, {}, {}, {}, {}\n".format(name,loc,id,day,query,doctor))
        self.setReminder(id,query,day,doctor,name)

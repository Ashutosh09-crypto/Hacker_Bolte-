import Hospital as H
import Doctor as D
import Patient as P
from flask import Flask,render_template,url_for,request,redirect



hospital1 = H.Hospital("Manipal Hospital Delhi", "Palam Vihar, Sector 6 Dwarka, Dwarka, New Delhi, Delhi 110075",'ManipalDelhi.txt',4.3,'011 4967 4967')
hospital2 = H.Hospital("Dharamsila Narayan Hospital","Metro Station, Dharamshila marg, Vasundhara Enclave Near Ashok Nagar, Dallupura, New Delhi, Delhi 110096",'Dharamsila.txt',4.3,'080675 06880')

hospital3 = H.Hospital("Bombay Hospital & Research Centre", "12,Vitthaldas Thackersey Marg, New Marine Lines,Mumbai 400020", 'BombayHospi.txt',4.5,'022 2206 7676')

# hospital1.displayDoctors()
# hospital2.displayDoctors()
# hospital3.displayDoctors()


hopitals = [hospital1,hospital2,hospital3]

def makeAppointment(patient,hospi, doctor):   #Clicking on submit button
    hospi.entryPatient(patient,doctor)
    #return "Thanks for visiting us!"

def newPatient(name, contact,email,loc,time, query):
    patient = P.Patient(name, contact, email, loc, time, query)

    if query == "Emergency":
        emergency(patient)
    elif query == "Online Consultancy":
        onlineConsult(patient)
    elif query == "Later Appointment":
        forAppointment(patient)
    makeAppointment(patient,hospital1,"Fatan Singh")



def emergency(patient):
    data = ''
    for hospital in hopitals:
        if patient.getLocation() in hospital.getLocation():
            data += "Hospital -> {}, HelpLine -> {}\n".format(hospital.getName(),hospital.getHelpLine())

    return data


def onlineConsult(patient):
    data = ''
    for hospital in hopitals:
        name,contact,depart,avai = hospital.displayDoctors()
        data += "Hospital -> {}, Doctor -> {}, Contact -> {}, Specialist -> {}, Time - {}\n".format(hospital.getName(),name,contact,depart,avai)

    return data




def forAppointment(patient):
    data = ''
    for hospital in hopitals:
        name, contact, depart, avai = hospital.displayDoctors()
        if patient.getLocation() in hospital.getLocation():
            data += "Hospital -> {},Location -> {},\n    Doctor -> {}, Contact -> {}, Specialist -> {}, Time - {}\n".format(hospital.getName(),hospital.getLocation(), name, contact, depart, avai)

    return data




app = Flask(__name__)
 
@app.route('/')
def home ():
    return render_template("Home.html")
 
@app.route('/patient')
def patientlog():
    return render_template('PatientLogin.html')

@app.route('/related1')
def related1():
    return render_template('COVID-19 Related.html')

@app.route('/related2')
def related2():
    return render_template('COVID-19 Related2.html')

@app.route('/related3')
def related3():
    return render_template('COVID-19 Related3.html')

@app.route('/related4')
def related4():
    return render_template('COVID-19 Related4.html')

@app.route('/related5')
def related5():
    return render_template('COVID-19 Related5.html')

@app.route('/Hospital')
def related6():
    return render_template('SearchHospitalNearMe.html')


@app.route('/validate', methods = ["POST"])
def validate():
    if request.method == 'POST':
        first_name = request.form['fname']
        # l_name = request.form['lname']
        contact = request.form['phone']
        email = request.form['email']
        loc = request.form['place']
        q = request.form['cause']
        time = request.form['days']

        newPatient(first_name, contact, email, loc, time, query=q)
        return redirect('/')
    else:
        return render_template('/')
 

if __name__ == '__main__':
    app.run(debug = True)


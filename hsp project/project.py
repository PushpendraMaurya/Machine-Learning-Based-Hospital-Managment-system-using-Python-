import mysql.connector as db
from multipledispatch import dispatch
import numpy as np
import matplotlib.pyplot as plt
import os 
import re

class Admin:

    def __init__(self):

        # This is try block use to create directory where store an account of certain datas such as receptionist , Doctor and Patient .
      


        # create database name is server...........
        mydb = db.connect(host='localhost', port='3306',
                          user='root', passwd='root')
        query = '''create database if not exists server;'''
        cur = mydb.cursor()
        cur.execute(query)
        mydb.close()

        # Admin Default Data
        self.a_id = 1
        self.a_username = 'admin'
        self.a_password = 'admin'
        self.AdminValue(self.a_id, self.a_username, self.a_password)

        # create table name is admin ..........
        self.connection()
        query = '''create table if not exists admin_pushpendra(
            a_id int primary key unique,
            a_username varchar(50) ,
            a_password varchar(50));'''

        self.cur.execute(query)
        self.mydb.close()

        # create table name is Receptionist ....
        self.connection()

    def AdminValue(self, a_id, a_username, a_password):
        self.connection()
        try:
            data = (a_id, a_username, a_password)
            query = '''insert into admin_pushpendra(a_id,a_username,a_password) values (%s,%s,%s);'''
            self.cur.execute(query, data)
            self.cur.execute("commit;")
            self.mydb.close()
        except:
            pass

    # This is is used to connect Python to Mysql in BasicDB as database name

    def connection(self):
        self.mydb = db.connect(host='localhost', user='root',
                               port='3306', passwd='root', database='server')
        self.cur = self.mydb.cursor()

    def AdminLogin(self, username, password):
        self.connection()
        data = (username,)
        query = '''select a_username,a_password from admin_pushpendra where a_username =%s;'''
        self.cur.execute(query, data)
        record = self.cur.fetchone()
        self.mydb.close()
        return record

    def ChangeAdminUserName(self,new_username,password):
        self.connection()
        data = (new_username,password)
        query = '''update admin_pushpendra set a_username = %s where a_password = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return "SuccessFully Admin Password Change !"
    
    def ChangeAdminPassword(self,new_password,password):
        self.connection()
        data = (new_password,password)
        query = '''update admin_pushpendra set a_password = %s where a_password = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return "SuccessFully Admin Password Change !"

    def checkpass(self,password):
        self.connection()
        data = (password,)
        query = '''select a_username,a_password from admin_pushpendra where a_password = %s; '''
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        self.mydb.close()
        return record

    # show the doctor info on without register info user
     
    def Skin_Doctor(self):
        self.connection()
        query ='''select dname,dqualification,dspecilist from Doctor where dspecilist in ('skin');'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        return record

    def Adult_Doctor(self):
        self.connection()
        query ='''select dname,dqualification,dspecilist from Doctor where dspecilist in ('adult');'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        return record
    
    def Child_Doctor(self):
        self.connection()
        query ='''select dname,dqualification,dspecilist from Doctor where dspecilist in ('child');'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        return record

    def Body_Doctor(self):
        self.connection()
        query ='''select dname,dqualification,dspecilist from Doctor where dspecilist in ('body');'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        return record

    def Women_Doctor(self):
        self.connection()
        query ='''select dname,dqualification,dspecilist from Doctor where dspecilist in ('women');'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        return record

    def ENT_Doctor(self):
        self.connection()
        query ='''select dname,dqualification,dspecilist from Doctor where dspecilist in ('ent');'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        return record

    def Show_ReceptionistInfo(self):
        self.connection()
        query='''select * from receptionist;'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        return record

# this function used for downlod text file data 
    def Downlod_Recept(self):
        self.connection()
        
        try:
            os.mkdir("Download")
        except:
            pass
        query = '''select * from receptionist;'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        return record

    # this is function used to Doctor create pandas through data 
    def Downlod_Doctor(self):
        self.connection()
        
        try:
            os.mkdir("Download")
        except:
            pass
        query = '''select * from doctor;'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        return record

    # this function used for patient downlod text file data 
    def Downlod_Patient(self):
        self.connection()
        
        try:
            os.mkdir("Download")
        except:
            pass
        query = '''select * from patient;'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        return record


    # this function used for Appointment downlod text file data 
    def Downlod_Appointment(self):
        self.connection()
        
        try:
            os.mkdir("Download")
        except:
            pass
        query = '''select * from patient;'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        return record

    # This is virtual Mode for admin only seen using Matplotlib and pandas ........
    def Virtual_Receptionist(self):
        self.connection()     
        query='''select rname,rage from receptionist;'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        return record

    # This is virtual Mode for admin only seen using Matplotlib and pandas ........
    def Virtual_Doctor(self):
        self.connection()
        query = '''select dname,dspecilist from doctor;'''
        self.cur.execute(query)
        record = self.cur.fetchall()
        return record 

    def Virtual_Patient(self):
        self.connection()
        query = '''select pname,ptreatment from patient;'''
        self.cur.execute(query)
        record = self.cur.fetchall()
        return record

    def Virtual_Appointment(self):
        self.connection()
        query = '''select Book_By,Patient_name from appointment;'''
        self.cur.execute(query)
        record = self.cur.fetchall()
        return record

    def AdminProfile(self,a_username):
        self.connection()
        data = (a_username,)
        query ='''select * from admin_pushpendra where a_username = %s;'''
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        return record

    def Delete_Receptionist(self,remail):
        self.connection()
        data = (remail,)
        query ='''delete from receptionist where remail = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        os.remove(f"Receptionist-Data/{remail}.txt")  # used to remove text file to created patient data inside folder
        return "Data SuccessFullly Deleted "

    def Delete_Doctor(self,demail):
        self.connection()
        data = (demail,)
        query ='''delete from doctor where demail = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        os.remove(f"Doctor-Data/{demail}.txt") # used to remove text file to created patient data inside folder
        return "Data SuccessFullly Deleted "

    def Delete_Patient(self,pemail):
        self.connection()
        data = (pemail,)
        query ='''delete from patient where pemail = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        os.remove(f"Patient-Data/{pemail}.txt")   # used to remove text file to created patient data inside folder
        return "Data SuccessFullly Deleted "
    
    def Delete_Appointment(self,appointment_id):
        self.connection()
        data = (appointment_id,)
        query ='''delete from appointment where appointment_id = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        # os.remove(f"AllFiles/{email}.txt")
        return "Data SuccessFullly Deleted "


    def check_receptionist_Info(self,rcontact = None, remail = None):
        self.connection()
        data = (rcontact , remail)
        query = '''select rcontact , remail from receptionist where rcontact = %s or remail = %s;'''
        self.cur.execute(query , data)
        record = self.cur.fetchone()
        self.mydb.close()
        # check receptionist already exists 
        if record == None:
            return True

        elif record[0] == rcontact:
            return f"\------------------This {rcontact}  Account  is Already Exists -------------------"
            # return False

        elif record[1] == remail:

            return  f"------------------This {remail}  Account  is Already Exists -------------------"
            # return False
   
    def check_doctor_info(self,demail = None):
        self.connection()
        data = (demail,)
        query = '''select demail from doctor where demail = %s;'''
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        self.mydb.close()
        if record == None:
            return True
        elif record[0] == demail:
            return f"------------------This {demail}  Account  is Already Exists -------------------"
            
    def check_patient_info(self,pemail = None, pcontact = None):
        self.connection()
        data = (pemail , pcontact)
        query = '''select pemail , pcontact from patient where pemail = %s or pcontact = %s;'''
        self.cur.execute(query , data)
        record = self.cur.fetchone()
        self.mydb.close()
        # check receptionist already exists 
        if record == None:
            return True

        elif record[0] == pemail:
            return f"------------------This {pemail}  Account  is Already Exists --------------------"
            # return False

        elif record[1] == pcontact:

            return  f"------------------This {pcontact}  Account  is Already Exists ------------------"
            # return False

    def check_doctor_available(self,dname):
        self.connection()
        data = (dname,)
        query = '''select dname from doctor where dname = %s;'''
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        self.mydb.close()
        # return record
        # print(record)
        return record

    def check_treatment_type(self,appoint_for):
        self.connection()
        data = (appoint_for,)
        query = '''select dspecilist from doctor where dspecilist = %s;'''
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        self.mydb.close()
      
        # print(record[0])
        return record
        

    def check_patient_matched(self,patient_name):
        self.connection()
        data = (patient_name,)
        query = '''select pname from patient where pname = %s;'''
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        self.mydb.close()
        # return record
        # print(record)
        return record

class Receptionist(Admin):
    
    def __init__(self):
        super().__init__()
        # create table name is receptionist
        self.connection()
        query = '''create table if not exists receptionist(
            rid int primary key auto_increment,
            rname varchar(50) not null,
            rcontact varchar(20) not null unique,
            rage int(3) not null,
            remail varchar(50) not null unique,
            raddress text,
            rpassword varchar(50));'''

        self.cur.execute(query)
        self.mydb.close()

    def R_CreateAccount(self, rname, rcontact, rage, remail, raddress, rpassword):
        self.connection()
        try:
            os.mkdir("Receptionist-Data")
        except:
            pass
        query = '''insert into receptionist(rname,rcontact,rage,remail,raddress,rpassword)
            values(%s,%s,%s,%s,%s,%s);'''
        data = (rname, rcontact, rage, remail, raddress, rpassword)
        self.cur.execute(query, data)
        self.cur.execute("commit;")
        self.mydb.close()
        return True
        # print("account created")

    def Receptionist_Login(self, remail, rpassword):
        self.connection()
        query = '''select remail from Receptionist where remail = %s && rpassword =%s;'''
        data = (remail, rpassword)
        self.cur.execute(query, data)
        record = self.cur.fetchone()
        self.mydb.close()
        return record

    def Check_Receptionist_Pass(self,rpassword):
        self.connection()
        data = (rpassword,)
        query = '''select a_username,a_password from receptionist where rpassword = %s;'''
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        self.mydb.close()
        return record

    def Show_DoctorInfo(self):
        self.connection()
        query ='''select * from Doctor;'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        return record
      
    def Show_PatientInfo(self):
        self.connection()
        # data =(dname,dqualification,dspecilist)
        query ='''select * from patient;'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        return record

    def ReceptionistProfile(self,remail):
        self.connection()
        data = (remail,)
        query = '''select * from receptionist where remail= %s ;'''
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        return record
    
    # here update method used for receptionist data only 
   
    @dispatch(str,str) #decorator used 
    def UpdateReceptionist(self,new_name,remail):
        self.connection()
        data = (new_name,remail)
        query ='''update Receptionist set rname = %s where remail =%s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
    
    @dispatch(int,str)
    def UpdateReceptionist(self,new_age,remail):
        self.connection()
        data = (new_age,remail)
        query ='''update Receptionist set rage = %s where remail =%s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
   
    @dispatch(str,str,str)
    def UpdateReceptionist(self,new_email,new_address,remail):
        self.connection()
        data = (new_email,new_address,remail)
        query = '''update Receptionist set remail = %s, raddress = %s where remail = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()

    @dispatch(str,str)
    def UpdateReceptionist(self,new_password,remail):
        self.connection()
        data = (new_password,remail)
        query = '''update Receptionist set rpassword = %s where remail = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()


    def Delete_DoctorAccount(self,demail):
        self.connection()
        data = (demail,)
        query ='''delete from doctor where demail = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return "Data SuccessFullly Deleted "

    def Delete_PatientAccount(self,pemail):
        self.connection()
        data = (pemail,)
        query ='''delete from patient where pemail = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return "Data SuccessFullly Deleted "

    # Delete Appointment Using Appintment Number 
    def Delete_AppointmentAccount(self,a_number):
        self.connection()
        data = (a_number,)
        query ='''delete from doctor where a_number = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return "Data SuccessFullly Deleted "

class Doctor(Receptionist):
    
    def __init__(self):
        super().__init__()

        # create doctor table name is Doctor.......
        self.connection()
        query = '''create table if not exists Doctor(
            did int primary key auto_increment ,
            dname varchar(50) not null,
            dage int(3) not null ,
            demail varchar(50) not null unique,
            dqualification varchar(100) not null,
            dspecilist varchar(50) not null,
            dpassword varchar(100) not null);'''

        self.cur.execute(query)
        # self.cur.execute("commit;")
        self.mydb.close()
        # return True
        # print("doctor table created ")

    def D_CreateAccount(self, dname, dage, demail, dqualification, dspecilist, dpassword):
        self.connection()
        # This is try block use to create directory where store an account of certain datas such as receptionist , Doctor and Patient .
        try:
            os.mkdir("Doctor-Data")
        except:
            pass
        query = '''insert into Doctor(dname,dage,demail,dqualification,dspecilist,dpassword)  values(%s,%s,%s,%s,%s,%s);'''
        data = (dname, dage, demail, dqualification, dspecilist, dpassword)
        self.cur.execute(query, data)
        self.cur.execute("commit;")
        self.mydb.close()
        return True
        # print("data inserted succesfully")

    def Doctor_Login(self, demail, dpassword):
        self.connection()
        query = '''select demail from Doctor where demail = %s && dpassword = %s;'''
        data = (demail, dpassword)
        self.cur.execute(query, data)
        record = self.cur.fetchone()
        self.mydb.close()
        return record
    
    def Patient_History(self):
        self.connection()
        query = '''select pname,page,pcontact,ptreatment from patient'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        return record
        
    def DoctorProfile(self,demail):
        self.connection()
        data = (demail,)
        query = '''select * from doctor where demail= %s ;'''
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        return record

    @dispatch(str,str)
    def UpdateDoctor(self,new_name,demail):
        self.connection()
        data = (new_name,demail)
        query = '''update Doctor set dname = %s where demail =%s'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
    
    @dispatch(int,str)
    def UpdateDoctor(self,new_age,demail):
        self.connection()
        data = (new_age,demail)
        query = '''update Doctor set dage = %s where demail =%s'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()

    @dispatch(str,str)
    def UpdateDoctor(self,new_email,demail):
        self.connection()
        data = (new_email,demail)
        query = '''update Doctor set demail = %s where demail =%s'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()

    # new_qualification,new_specialist
    @dispatch(str,str,str)
    def UpdateDoctor(self,new_qualification,new_specialist,demail):
        self.connection()
        data = (new_qualification,new_specialist,demail)
        query = '''update Doctor set dqualification  = %s, dspecilist = %s where demail =%s'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
    
    @dispatch(str,str)
    def UpdateDoctor(self,new_password,demail):
        self.connection()
        data = (new_password,demail)
        query = '''update Doctor set dpassword = %s where demail =%s'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()

class Patient(Doctor):
    
    def __init__(self):
        super().__init__()

        # create table patient name is Patient..........
        self.connection()
        query = ''' create table if not exists Patient(
                pid int primary key auto_increment ,
                pname varchar(50) not null ,
                pemail varchar(100) not null,
                page int(3) not null,
                pcontact bigint not null,
                ptreatment varchar(50) not null,
                ppassword varchar(50) not null);'''

        self.cur.execute(query)
        self.mydb.close()

    def P_CreateAccount(self, pname, pemail, page, pcontact,ptreatment, ppassword):
        self.connection()
         # This is try block use to create directory where store an account of certain datas such as receptionist , Doctor and Patient .
        try:
            os.mkdir("Patient-Data")
        except:
            pass
        query = '''insert into Patient(pname,pemail,page,pcontact,ptreatment,ppassword) values(%s,%s,%s,%s,%s,%s);'''
        data = (pname, pemail, page, pcontact,ptreatment, ppassword)
        self.cur.execute(query, data)
        self.cur.execute("commit;")
        self.mydb.close()
        return True

    def Patient_Login(self, pemail, ppassword):
        self.connection()
        query = '''select pemail from Patient where pemail = %s && ppassword = %s;'''
        data = (pemail, ppassword)
        self.cur.execute(query, data)
        record = self.cur.fetchone()
        self.mydb.close()
        return record

    def PatientProfile(self,pemail):
        self.connection()
        data = (pemail,)
        query = '''select * from patient where pemail=%s'''
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        return record

    @dispatch(str,str)
    def UpdatePatient(self,new_email,pemail):
        self.connection()
        data = (new_email,pemail)
        query = '''update Patient set pemail = %s where pemail=%s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()

    @dispatch(str,str)
    def UpdatePatient(self,new_contact,pemail):
        self.connection()
        data = (new_contact,pemail)
        query = '''update Patient set pcontact = %s where pemail=%s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()

    @dispatch(str,str)
    def UpdatePatient(self,new_password,pemail):
        self.connection()
        data = (new_password,pemail)
        query = '''update Patient set ppassword = %s where pemail=%s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()


    @dispatch(str,str,str,str)
    def UpdatePatient(self,new_email,new_contact,new_password,pemail):
        self.connection()
        data = (new_email,new_contact,new_password,pemail)
        query = '''update Patient set pemail = %s,pcontact=%s,ppassword=%s where pemail=%s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()

class Appintment(Patient):
    
    def __init__(self):
        super().__init__()
        # create   table name is Appointment 
        self.connection()
        query = '''create table if not exists appointment(
            appointment_id int primary key auto_increment,
            appointment_for varchar(50) not null ,
            Doctor_name varchar(50) not null,
            Patient_name varchar(50) not null,
            identity varchar(50) default "Patient",
            Book_By varchar(50)  not null ,
            Apppintment_date date not null );'''

        self.cur.execute(query)
        self.mydb.close()

    def Book_Appointment(self,appoint_for,doctor_name,patient_name,Book_By,identity):
        self.connection()
        try:
            os.mkdir("Appointment-Data")
        except:
            pass
        
        data = (appoint_for,doctor_name,patient_name,Book_By,identity)
        query = '''insert into appointment (appointment_for,Doctor_name,patient_name,identity,Book_By,Apppintment_date) values (%s,%s,%s,%s,%s,now());'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return True
       

    #,appointment_id,appointment_for,Doctor_name,Book_By,Apppintment_date
    def View_Appointment(self):
        self.connection()
        query= '''select * from appointment ;'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        return record

    # view all the patient appointment booked  to particular dates ......
    def Appointment_Alocated_Patient(self,pemail):
        self.connection()
        data = (pemail,)
        query = '''select pname from patient where pemail = %s;'''
        self.cur.execute(query , data)
        pname = self.cur.fetchone()
        pname = pname[0]
        # print(pname)
        self.mydb.close()


        self.connection()
        data = (pname,)
        query = '''select *  from appointment where Patient_name = %s'''
        self.cur.execute(query,data)
        record = self.cur.fetchall()
        return record 
        # print(record)




    
    # view all the patient appointment booked  to particular doctor ......
    def Appointment_Alocate_Doctor(self,demail):
        #this is function to fetch doctor name 
        self.connection()
        data = (demail,)
        query = '''select dname from doctor where demail = %s;'''
        self.cur.execute(query , data)
        dname = self.cur.fetchone()
        dname = dname[0]
        # print(dname)
        self.mydb.close()

        # this function to use fetched doctor email where  in doctor tabled fetched doctor name if matechd doctor email then fetch doctor appointed patient list 
         
        self.connection()
        data = (dname,)
        query = '''select *  from appointment where Doctor_name = %s'''
        self.cur.execute(query,data)
        record = self.cur.fetchall()
        return record 
        

    def check_Doctor(self,doctor_name):
        self.connection()
        data = (doctor_name,)
        query = '''select dname for doctor  where dname = %s'''
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        self.mydb.close()
        return record
       
class Regx(Appintment):

    def __init__(self):
        super().__init__()
    
    def Receptionist_NameValidation(self,rname):
        p = "^[a-zA-Z\ ]+$"
        if re.match(p,rname):
            return True
        else:
            return False

    def Doctor_NameValidation(self,dname):
        p = "^[a-zA-Z\ ]+$"
        if re.match(p,dname):
            return True
        else:
            return False

    def Patient_NameValidation(self,pname):
        p = "^[a-zA-Z\ ]+$"
        if re.match(p,pname):
            return True
        else:
            return False


    def Receptionist_ContactValidation(self,rcontact):
        p = "^[6-9]\d{9}"
        if re.match(p,rcontact):
            return True
        else:
            return False

    def Patient_ContactValidation(self,pcontact):
        p = "^[6-9]\d{9}"
        if re.match(p,pcontact):
            return True
        else:
            return False


    def Receptionist_AgeValidation(self,rage):
        p = rage.isdigit()
        if p == True:
            return True
        else:
            return False

    def Doctor_AgeValidation(self,dage):
        p = dage.isdigit()
        if p == True:
            return True
        else:
            return False

    def Patient_AgeValidation(self,page):
        p = page.isdigit()
        if p == True:
            return True
        else:
            return False

    
   
 

    def Receptionist_EmailValidation(self,remail):
        p = "^[a-zA-Z0-9\_\.]+@[a-z]+\.[a-z]+$"
        if re.match(p,remail):
            return True
        else:
            return False

    def Doctor_EmailValidation(self,demail):
        p = "^[a-zA-Z0-9\_\.]+@[a-z]+\.[a-z]+$"
        if re.match(p,demail):
            return True
        else:
            return False

    def Patient_EmailValidation(self,pemail):
        p = "^[a-zA-Z0-9\_\.]+@[a-z]+\.[a-z]+$"
        if re.match(p,pemail):
            return True
        else:
            return False



App = Regx()

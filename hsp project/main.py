import mysql.connector as db
from project import Regx
from prettytable import PrettyTable
import time
from datetime import datetime
import  matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
App = Regx()


while True:
    print("\n<------------------->  :::::: Hospital Management System  ::::::: <--------------------->\n")
    print("\n1- Admin Login \n2- Receptionist Login \n3- Doctor Login \n4- Patient Login \n5- TreatMent Type  \n6- Exit\n")
    ch = input("Enter Your Choice :")
    # Admin Login ............... # Done Code  ,  #Done Create Another File Data , #Done Virtual Code , #Pending REgx
    
    if (ch == "1"):
        print("\n----------------------------------------- Admin Login Section -----------------------------------------\n")
        a_username = input("Enter Your UserName : ")
        a_password = input("Enter Your Password : ")
        admin = App.AdminLogin(a_username, a_password)      
        ti =time.strftime("%Y-%m-%d %H:%M")
        if admin == None:
            print("\n*************** Invalid UserName ***********\n")

        else:
            if a_password != admin[1]:
                print("\n******** Invalid Password ************\n")
            else:
                
                print("\n----------------------------------------- SuccessFully Logged IN  -----------------------------------------\n")
                print(f"\nHello {a_username} Welcome to Our Hospital {ti}\n")
                # Admin Authentication section .............
                while True:
                    print("\n----------------------------------------- Admin Section  -----------------------------------------\n")
                    print("\n1- Virtual Mode \n2- Profile \n3- Add Accounts  \n4- Remove Accounts \n5- View Accounts \n6- Appointments \n7- Log out \n")
                    
                    ach = input("Enter Your Admin Choice : ")
                   
                    #  If press 1 then you go inside virtual mode using admin throwgh view all account info in using machine learning part  
            
                    if(ach=="1"):      #Code Error Checked 
                        print("\n--------------------- Virtual Mode Section ---------------------------\n")
                        print("\n1- View Virtual Records \n2- Download Records \n3- Exit Virtual Mode \n")
                        virtual_choice = input("Enter Virtual Mode Choice :")
                        while True :
                            #view all accounts in  virtual Mode   here   # Done Code 
                            print("\n---------------------- This is Virtual Vishulization Mode --------------------------------\n")
                            if (virtual_choice =="1"):
                                print("\n1- Virtual Receptionist Mode \n2- Virtual Doctor Mode \n3- Virtual Patient Mode \n4- Virtual Appintment Mode \n5- Exit Virtual Mode\n")
                                virtual_Ch = input("Enter Virtual Mode Choice :")

                                #  This is virtual mode where i show the all the receptionist register in  hospital 
                            
                                if(virtual_Ch=="1"):
                                    print("\n-------------------------------- Virtual Receptionoist Mode ----------------------------------\n")
                                    print("\nVishuliZation Mode has Opened , Please Wait ....................\n")
                                    rname =[]
                                    rage =[]
                                    x = App.Virtual_Receptionist()
                                    
                                    for i in x:
                                        
                                        rname.append(i[0])
                                        rage.append(i[1])  

                                    plt.bar(rname,rage)
                                    # plt.ylim(1,100)
                                    plt.xlabel("Name of Receptionist")
                                    plt.ylabel("Age Of Receptionist ")
                                    plt.title("Receptionist Name & Age Information")
                                    plt.show()
                                
                                #  This is virtual mode where i show the all the doctor register in  hospital 
                                elif(virtual_Ch=="2"):
                                    print("-------------------------------- Virtual Receptionoist Mode ----------------------------------")
                                    print("\nVishuliZation Mode has Opened , Please Wait ....................\n")
                                    dname =[]
                                    dspecilist =[]
                                    x = App.Virtual_Doctor()
                                    
                                    for i in x:
                                        
                                        dname.append(i[0])
                                        dspecilist.append(i[1])  

                                    plt.bar(dname,dspecilist)
                                    # plt.ylim(1,20)
                                    plt.xlabel("Name of Doctor")
                                    plt.ylabel("Specilist of Doctor ")
                                    plt.title("Doctor  Name & Specialist Information")
                                    plt.show()

                                # here patient mode 
                                elif(virtual_Ch=="3"):
                                    print("\n-------------------------------- Virtual Patient Mode ----------------------------------\n")
                                    print("\nVishuliZation Mode has Opened , Please Wait ....................\n")
                                    pname =[]
                                    ptreatment =[]
                                    x = App.Virtual_Patient()
                                    
                                    for i in x:
                                        
                                        pname.append(i[0])
                                        ptreatment.append(i[1])  

                                    plt.bar(pname,ptreatment)
                                    # plt.ylim(1,100)
                                    plt.xlabel("Name of Patient")
                                    plt.ylabel("Treatment type of Patient ")
                                    plt.title("Patient Name & Treatment Information")
                                    plt.show()
                                
                                elif(virtual_Ch=="4"):
                                    print("\n-------------------------------- Virtual Appointment Mode ----------------------------------\n")
                                    print("\nVishuliZation Mode has Opened , Please Wait ....................\n")
                                    Book_By =[]
                                    Patient_name =[]
                                    x = App.Virtual_Appointment()
                                    
                                    for i in x:
                                        
                                        Book_By.append(i[0])
                                        Patient_name.append(i[1])  

                                    plt.bar(Book_By,Patient_name)
                                    # plt.ylim(1,20)
                                    plt.xlabel("Appointment Booked By ")
                                    plt.ylabel("Name  of Patient  ")
                                    plt.title("Appointment Booked & Name  of Patient Information")
                                    plt.show()
                                    
                                elif(virtual_Ch=="5"):
                                    print("\n-------------------------------- Exit the Virtual  Mode ----------------------------------\n")
                                    break
                                
                                else:
                                    print("\n-------------------------------- invalid Choice to Virtual Mode  ----------------------------------\n")
                            
                            # here code is downlod all code as registered users 
                            elif (virtual_choice =="2"):
                                print("\n------------------------------ Downlod Records ------------------------------------\n")
                                print("\n1- Receptionist Data \n2-Doctor Data \n3-Patient Data \n4- Appointment Data \n5- Exit \n")
                                data = input("Enter Your CHoice : ")
                                # while True: 
                                if(data =="1"):
                                    print("--------------------Receptionist Downlod Section ----------------------------")
                                    print("\n1-TEXT Format \n2-CSV Format \n3- JSON Format \n4- EXCEL Format \n5- Exit For Downlod Mode \n")
                                    r = input("Enter Your Downlod Choice :")
                                    if(r =="1"):
                                        print("\nTEXT Format data has Generated....................................... \n")
                                        rid = []
                                        rname = []
                                        rcontact = []
                                        rage = []
                                        remail = []
                                        raddress = []
                                        rpassword = []
                                        view = App.Downlod_Recept()
                                        for i in  view:
                                            rid.append(i[0])
                                            rname.append(i[1])
                                            rcontact.append(i[2])
                                            rage.append(i[3])
                                            remail.append(i[4])
                                            raddress.append(i[5])
                                            rpassword.append(i[6])
                                        # here code is create the whole the receptionist data in tet format 
                                        with open(f"Download/receptionist.txt" , "a") as file:
                                            file.write(" \n*-------------------*-------------------*---------*-------------------*--------------*-----*This is Receptionist Information *-------------------*-------------------*-----------*--------*\n")
                                            file.write(f"\n*-------------------*-------------------*---------*-------------------*--------------*------*--------------------*-----------*-------------------*-------------------*-----------*--------*\n")
                                            file.write(f"Receptionist ID :- {rid}\n")
                                            file.write(f"Receptionist Name :- {rname}\n")                             
                                            file.write(f"Receptionist Contact :- {rcontact}\n")                                 
                                            file.write(f"Receptionist Age :- {rage}\n")                                   
                                            file.write(f"Receptionist Email :- {remail}\n")                               
                                            file.write(f"Receptionist Address :- {raddress}\n")
                                            file.write(f"Receptionist Password :- {rpassword}\n")
                                            file.write(f"\n-------------------*-------------------*---------*-----------Your Information End---------------------*-----------*-------------------*-------------------*-----------*--------*-----------*\n")
                                        

                                    elif(r=="2"):
                                        print("\nCSV Formate data has Generated....................................... \n")
                                        print("\nCSV Format Data.......................................\n")
                                        record = App.Downlod_Recept()
                                        df = pd.DataFrame(record, columns=['Receptionist ID ','Receptionist Name','Receptionist Contact','Receptionist Age','Receptionist Email','Receptionist Address','Receptionist Password'])
                                        df.to_csv("Download/Receptionist_info.csv") # if index = False when i want not indexx postion

                                    elif(r=="3"):
                                        print("\nJSON Formate data has Generated....................................... \n")
                                        record = App.Downlod_Recept()
                                        df = pd.DataFrame(record, columns=['Receptionist ID ','Receptionist Name','Receptionist Contact','Receptionist Age','Receptionist Email','Receptionist Address','Receptionist Password'])
                                        df.to_json("Download/Receptionist_info.json")

                                    elif(r=="4"):
                                        print("\nEXCEL Formate data has Generated....................................... \n")
                                        print("\nExcel Format Data Generated...........................\n")
                                        record = App.Downlod_Recept()
                                        df = pd.DataFrame(record, columns=['Receptionist ID ','Receptionist Name','Receptionist Contact','Receptionist Age','Receptionist Email','Receptionist Address','Receptionist Password'])
                                        df.to_excel("Download/Receptionist_info.xlsx")

                                    elif(r=="5"):
                                        print("\n-----------------------Thank You Receptionist Downlod Mode -----------------------------------\n")
                                        
                                    else:
                                        print("\n----------------------- Invalid Choice -----------------------------------\n")




                                elif(data =="2"):
                                    print("\n------------------ Doctor Downlod Section -------------------------\n")
                                    print("\n1-TEXT Format \n2-CSV Format \n3- JSON Format \n4- EXCEL Format \n5- Exit For Downlod Mode \n")
                                    r = input("Enter Your Downlod Choice :")
                                    if(r =="1"):
                                        print("\nTEXT Formate data has Generated....................................... \n")
                                        #did | dname            | dage | demail               | dqualification | dspecilist | dpassword 
                                        did = []
                                        dname = []
                                        dage = []
                                        demail = []
                                        dqualification = []
                                        dspecilist = []
                                        dpassword = []
                                        view = App.Downlod_Doctor()
                                        for i in  view:
                                            did.append(i[0])
                                            dname.append(i[1])
                                            dage.append(i[2])
                                            demail.append(i[3])
                                            dqualification.append(i[4])
                                            dspecilist.append(i[5])
                                            dpassword.append(i[6])
                                        # here code is create the whole the receptionist data in tet format 
                                        with open(f"Download/Doctor.txt" , "a") as file:
                                            file.write(" \n*-------------------*-------------------*---------*-------------------*--------------*-----*This is Doctor Information *-------------------*-------------------*-----------*--------*----------------*------------------*\n")
                                            file.write(f"\n*-------------------*-------------------*---------*-------------------*--------------*------*--------------------*-----------*-------------------*-------------------*-----------*--------*------------*-----------------*\n")
                                            file.write(f"Doctor ID :- {did}\n")
                                            file.write(f"Doctor Name :- {dname}\n")                             
                                            file.write(f"Doctor Age :- {dage}\n")                                 
                                            file.write(f"Doctor Email :- {demail}\n")                                   
                                            file.write(f"Doctor Qualification :- {dqualification}\n")                               
                                            file.write(f"Doctor Specialist :- {dspecilist}\n")
                                            file.write(f"Doctor Password :- {dpassword}\n")
                                            file.write(f"\n*-------------------*-------------------*---------*-------------------*--------------*-----*This is Doctor Information *-------------------*-------------------*-----------*--------*----------------*---------------------*\n")



                                    elif(r=="2"):
                                        print("\nCSV Formate data has Generated....................................... \n")
                                        print("\nCSV Format Data.......................................\n")
                                        record = App.Downlod_Doctor()
                                        df = pd.DataFrame(record, columns=['Doctor ID','Doctor Name','Doctor Age','Doctor Email','Doctor Qualification','Doctor Specialist','Doctor Password '])
                                        df.to_csv("Download/doctor_info.csv") # if index = False when i want not indexx postion

                                    elif(r=="3"):
                                        print("\nJSON Formate data has Generated....................................... \n")
                                        print("\nJSON Format Data  Generated............................\n") 
                                        record = App.Downlod_Doctor()
                                        df = pd.DataFrame(record, columns=['Doctor ID','Doctor Name','Doctor Age','Doctor Email','Doctor Qualification','Doctor Specialist','Doctor Password '])
                                        df.to_json("Download/doctor_info.json")

                                    elif(r=="4"):
                                        print("\nEXCEL Formate data has Generated....................................... \n")
                                        print("\nExcel Format Data Generated...........................\n")
                                        record = App.Downlod_Doctor()
                                        df = pd.DataFrame(record, columns=['Doctor ID','Doctor Name','Doctor Age','Doctor Email','Doctor Qualification','Doctor Specialist','Doctor Password '])
                                        df.to_excel("Download/doctor_info.xlsx")

                                    elif(r=="5"):
                                        print("\n-----------------------Thank You Receptionist Downlod Mode -----------------------------------\n")
                                        if(r =="1"):
                                            print("\nTEXT Formate data has Generated....................................... \n")
                                            #did | dname            | dage | demail               | dqualification | dspecilist | dpassword 
                                            did = []
                                            dname = []
                                            dage = []
                                            demail = []
                                            dqualification = []
                                            dspecilist = []
                                            dpassword = []
                                            view = App.Downlod_Doctor()
                                            for i in  view:
                                                did.append(i[0])
                                                dname.append(i[1])
                                                dage.append(i[2])
                                                demail.append(i[3])
                                                dqualification.append(i[4])
                                                dspecilist.append(i[5])
                                                dpassword.append(i[6])
                                            # here code is create the whole the receptionist data in tet format 
                                            with open(f"Download/Doctor.txt" , "a") as file:
                                                file.write("\n*-------------------This is Doctor Information  ------------*-----------*\n")
                                                file.write(f"\n*--------------*-----------------*-----------*----------*\n")
                                                file.write(f"Doctor Name :- {did}\n")
                                                file.write(f"Doctor Contact :- {dname}\n")                             
                                                file.write(f"Doctor Age :- {dage}\n")                                 
                                                file.write(f"Doctor Email :- {demail}\n")                                   
                                                file.write(f"Doctor Address :- {dqualification}\n")                               
                                                file.write(f"Doctor Password :- {dspecilist}\n")
                                                file.write(f"Doctor Password :- {dpassword}\n")
                                                file.write(f"\n*--------------*------ Your Information End ---------*----------------*\n")



                                        elif(r=="2"):
                                            print("\nCSV Formate data has Generated....................................... \n")
                                            print("\nCSV Format Data.......................................\n")
                                            record = App.Downlod_Doctor()
                                            df = pd.DataFrame(record, columns=['id','name','joined date','salary','designation','contact','pass'])
                                            df.to_csv("Download/doctor_info.csv") # if index = False when i want not indexx postion

                                        elif(r=="3"):
                                            print("\nJSON Formate data has Generated....................................... \n")
                                            print("\nJSON Format Data  Generated............................\n") 
                                            record = App.Downlod_Doctor()
                                            df = pd.DataFrame(record, columns=['id','name','joined date','salary','designation','contact','pass'])
                                            df.to_json("Download/doctor_info.json")

                                        elif(r=="4"):
                                            print("\nEXCEL Formate data has Generated....................................... \n")
                                            print("\nExcel Format Data Generated...........................\n")
                                            record = App.Downlod_Doctor()
                                            df = pd.DataFrame(record, columns=['id','name','joined date','salary','designation','contact','pass'])
                                            df.to_excel("Download/doctor_info.xlsx")

                                        elif(r=="5"):
                                            print("\n-----------------------Thank You Receptionist Downlod Mode -----------------------------------\n")
                                            
                                        else:
                                            print("\n----------------------- Invalid Choice -----------------------------------\n")

                                        
                                    else:
                                        print("\n----------------------- Invalid Choice -----------------------------------\n")

                                elif(data =="3"):
                                    print("\n------------------ Patient Downlod Section -------------------------\n")
                                    print("\n1-TEXT Format \n2-CSV Format \n3- JSON Format \n4- EXCEL Format \n5- Exit For Downlod Mode \n")
                                    r = input("Enter Your Downlod Choice :")
                                    if(r =="1"):
                                        print("\nTEXT Format data has Generated....................................... \n")
                                        #| pid | pname        | pemail            | page | pcontact   | ptreatment | ppassword 
                                        pid = []
                                        pname = []
                                        pemail = []
                                        page = []
                                        pcontact = []
                                        ptreatment = []
                                        ppassword = []
                                        view = App.Downlod_Patient()
                                        for i in  view:
                                            pid.append(i[0])
                                            pname.append(i[1])
                                            pemail.append(i[2])
                                            page.append(i[3])
                                            pcontact.append(i[4])
                                            ptreatment.append(i[5])
                                            ppassword.append(i[6])
                                        # here code is create the whole the Patient data in tet format 
                                        with open(f"Download/Patient.txt" , "a") as file:
                                            file.write(" \n*-------------------*-------------------*---------*-------------------*--------------*-----*This is Patient Information *-------------------*-------------------*-----------*--------*----------------*------------------*\n")
                                            file.write(f"\n*-------------------*-------------------*---------*-------------------*--------------*------*--------------------*-----------*-------------------*-------------------*-----------*--------*------------*-----------------*\n")
                                            file.write(f"Patient ID :- {pid}\n")
                                            file.write(f"Patient Name :- {pname}\n")                             
                                            file.write(f"Patient Email :- {pemail}\n")                                 
                                            file.write(f"Patient Age :- {page}\n")                                   
                                            file.write(f"Patient Contact :- {pcontact}\n")                               
                                            file.write(f"Patient Treatment :- {ptreatment}\n")
                                            file.write(f"Patient Password :- {ppassword}\n")
                                            file.write(f"\n*--------------*------ Your Information End ---------*----------------*\n")



                                    elif(r=="2"):
                                        print("\nCSV Formate data has Generated....................................... \n")
                                        print("\nCSV Format Data.......................................\n")
                                        record = App.Downlod_Patient()
                                        df = pd.DataFrame(record, columns=['Patient ID','Patient Name','Patient Email','Patient Age','Patient Contact','Patient Treatment','Patient Password'])
                                        df.to_csv("Download/Patient_info.csv") # if index = False when i want not indexx postion

                                    elif(r=="3"):
                                        print("\nJSON Formate data has Generated....................................... \n")
                                        record = App.Downlod_Patient()
                                        df = pd.DataFrame(record, columns=['Patient ID','Patient Name','Patient Email','Patient Age','Patient Contact','Patient Treatment','Patient Password'])
                                        df.to_json("Download/Patient_info.json")

                                    elif(r=="4"):
                                        print("\nEXCEL Formate data has Generated....................................... \n")
                                        record = App.Downlod_Patient()
                                        df = pd.DataFrame(record, columns=['Patient ID','Patient Name','Patient Email','Patient Age','Patient Contact','Patient Treatment','Patient Password'])
                                        df.to_excel("Download/Patient_info.xlsx")

                                    elif(r=="5"):
                                        print("\n-----------------------Thank You Receptionist Downlod Mode -----------------------------------\n")
                                        
                                    else:
                                        print("\n----------------------- Invalid Choice -----------------------------------\n")


                                elif(data =="4"):
                                    print("\n------------------ Appointment Downlod Section -------------------------\n")
                                    print("\n1-TEXT Format \n2-CSV Format \n3- JSON Format \n4- EXCEL Format \n5- Exit For Downlod Mode \n")
                                    r = input("Enter Your Downlod Choice :")
                                    if(r =="1"):
                                        print("\nTEXT Formate data has Generated....................................... \n")
                                    #appointment_id | appointment_for | Doctor_name | Patient_name | identity             | Book_By      | Apppintment_date
                                        appointment_id = []
                                        appointment_for = []
                                        Doctor_name = []
                                        Patient_name = []
                                        identity = []
                                        Book_By = []
                                        Apppintment_date = []
                                        view = App.Downlod_Appointment()
                                        for i in  view:
                                            appointment_id.append(i[0])
                                            appointment_for.append(i[1])
                                            Doctor_name.append(i[2])
                                            Patient_name.append(i[3])
                                            identity.append(i[4])
                                            Book_By.append(i[5])
                                            Apppintment_date.append(i[6])
                                        # here code is create the whole the receptionist data in tet format 
                                        with open(f"Download/Appointment_info.txt" , "a") as file:
                                            file.write("*-------------------*-------------------*---------*-------------------*--------------*-----*This is Patient Information *-------------------*-------------------*----*\n")
                                            file.write("\n*-------------------*-------------------*---------*-------------------*--------------*-----*-----------------------------*-------------------*-------------------*\n")
                                            file.write(f"Appointment ID :- {appointment_id}\n")
                                            file.write(f"Apppintment for Contact :- {appointment_for}\n")                             
                                            file.write(f"Doctor Name :- {Doctor_name}\n")                                 
                                            file.write(f"Patient Name :- {Patient_name}\n")                                   
                                            file.write(f"Appointment Identity :- {identity}\n")                               
                                            file.write(f"Appointment Booked By  :- {Book_By}\n")
                                            file.write(f"Appointment Date :- {Apppintment_date}\n")
                                            file.write(f"\n*--------------*------ Your Information End ---------*----------------*\n")



                                    elif(r=="2"):
                                        print("\nCSV Formate data has Generated....................................... \n")
                                        print("\nCSV Format Data.......................................\n")
                                        record = App.Downlod_Appointment()
                                        df = pd.DataFrame(record, columns=['Appointment ID','Apppintment for Contact','Doctor Name','Patient Name','Appointment Identity','Appointment Booked By','Appointment Date'])
                                        df.to_csv("Download/Appointment_info.csv") # if index = False when i want not indexx postion

                                    elif(r=="3"):
                                        print("\nJSON Formate data has Generated....................................... \n")
                                        print("\nJSON Format Data  Generated............................\n") 
                                        record = App.Downlod_Appointment()
                                        df = pd.DataFrame(record, columns=['Appointment ID','Apppintment for Contact','Doctor Name','Patient Name','Appointment Identity','Appointment Booked By','Appointment Date'])
                                        df.to_json("Download/Appointment_info.json")

                                    elif(r=="4"):
                                        print("\nEXCEL Formate data has Generated....................................... \n")
                                        print("\nExcel Format Data Generated...........................\n")
                                        record = App.Downlod_Appointment()
                                        df = pd.DataFrame(record, columns=['Appointment ID','Apppintment for Contact','Doctor Name','Patient Name','Appointment Identity','Appointment Booked By','Appointment Date'])
                                        df.to_excel("Download/Appointment_info.xlsx")

                                    elif(r=="5"):
                                        print("\n-----------------------Thank You Receptionist Downlod Mode -----------------------------------\n")
                                        
                                    else:
                                        print("\n----------------------- Invalid Choice -----------------------------------\n")


                                    
                                elif(data =="5"):
                                    print("\n-------------------------------- Thank You Downlod section -----------------------------------------\n")
                                    break
                                else:
                                    print("\n------------------------ invalid Download Option ,try Again -----------------------\n")
                            

                            elif (virtual_choice=="3"):
                                print("\n-------------------Exit The Virtual Mode Section ---------------------------\n")
                                break

                            else:
                                print("\n------------------------- Exit Virtual Mode --------------------------------\n")
                            
                    
                    # view admin profile  # Done Code 
                    elif(ach =="2"):
                        while True:
                            print("\n------------------------ This is Admin Information Section -----------------------------\n")
                            print("\n1- View Admin Information \n2- Change Admin Information \n3- Exit")
                            admin_info = input("Enter Admin Information  Choice : ")
                            #view admin profile code 
                            if (admin_info =="1"):  
                                print("\n----------------------------------------- View Admin  Profile   -----------------------------------------\n")
                                admin_Profile = App.AdminProfile(a_username,)
                                x = PrettyTable()
                                x.field_names = ["Receptionist  ID","Receptionist UserName","Receptionist Password"]
                                x.add_row(admin_Profile)
                                print(x)  
                            # change admin informtion  code 
                            elif (admin_info =="2"):
                                while True:
                                # Change Admin Account ....... # Done Code
                                    # print("\n----------------------------------------- Change Admin Account -----------------------------------------\n")
                                    print("\n--------------------- Change Admin Information Section ------------------------\n")
                                   
                                    print("\n1- Change Admin UserName \n2- Change Admin Password \n3- Exit\n")
                                    a_change = input("Enter Your Choice :")
                                    
                                     # Change Admin   account  Username 
                                    if (a_change == "1"):
                                        password = input("Enter Current Passsword : ")
                                        x = App.checkpass(password)
                                        if x == None:
                                            print("\n----------------------------------------- Invalid Password -----------------------------------------\n")
                                            
                                        else:
                                            new_username = input("Enter Your New UserName :")
                                        
                                            x1 = App.ChangeAdminUserName( new_username, password)
                                            
                                            print(f"\n---------------------- {x1} ---------------------\n")
                                    
                                    # change admin account passswod 
                                    elif (a_change == "2"):
                                        password = input("Enter Current Password :")
                                        x = App.checkpass(password)
                                        if x == None:
                                            print("\n----------------------------------------- Invalid Admin Password -----------------------------------------n")
                                            
                                        else:
                                            new_password = input("Enter New Password :")
                                            x2 = App.ChangeAdminPassword(new_password, password)
                                            
                                            print(f"\n----------------------- {x2} --------------------\n")
                                    
                                    elif (a_change == "3"):
                                        print("\n-----------------------------------------Thank You Admin Info Section -----------------------------------------\n")
                                        break
                                    
                                    else:
                                        print("\n------------------------------------- Invalid Choice ---------------------------------------------\n")            
                                
                            elif (admin_info =="3"):
                                print("\n-----------------------------------------Thank You Admin Information Section -----------------------------------------\n")
                                break
                            
                            else:
                                print("\n------------------------------------- Invalid Choice ---------------------------------------------\n")
                
                    # Add Receptionist / Doctor/ Patient / Appointment  Section ....... # Done Code
                    elif(ach =="3"):
                        # while True:
                        print("\n--------------- Add Receptionist / Doctor / Patient Account -------------------\n")
                        print("\n1- Receptionist Account \n2- Doctor Account \n3- Patient Account \n4- Exit \n")
                        add_account = input("Enter Create Account Type : ")
                        while True:
                            #  add receptionist account  #Done Full Validation
                            if (add_account == "1"):
                                print("\n----------------------------------------- Add Receptionist Account -----------------------------------------\n")    
                                # Name Validation 
                                while True:
                                    rname = input("Enter Receptionist Name : ")
        
                                    x = App.Receptionist_NameValidation(rname)
                                    if x == True:  
                                        break
                            
                                    # Contact Validation 
                                while True:

                                    rcontact = input("Enter Receptionist Contact : ")
                                    x = App.Receptionist_ContactValidation(rcontact)
                                    if x == True:
                                        break
                                    else:
                                        print("------Invalid COntact Format ---------")
                                                
                                while True:
                                    rage = input("Enter Receptionist Age : ")
                                    x = App.Receptionist_AgeValidation(rage)
                                    if x == True:
                                        break
                                    else:
                                        print("-------invalid Age ---------")
                                
                                while True:
                                    remail = input("Enter receptionist Email :")
                                    x = App.Receptionist_EmailValidation(remail)
                                    if x ==True:
                                        break
                                    else:
                                        print("------Invalid Receptionist Email------")
                            
                                raddress = input("Enter Receptionist Address :")

                                rpassword = input("Enter Receptionist Password :")
                                
                                check_receptionist = App.check_receptionist_Info(rcontact,remail)
                                if check_receptionist == True:  

                                    r_account = App.R_CreateAccount(rname, rcontact, rage, remail, raddress, rpassword)
                                    if r_account == True:  
                                        # here print whole the receptionist data into the another folder name is receptionist 
                                        with open(f"Receptionist-Data/{remail}.txt" , "a") as file:
                                            file.write("\n*-------------------This is Receptionist Information  ------------*-----------*\n")
                                            file.write(f"\n*--------------*-------Welcome to MR/Mrs .{rname}----------*-----------*----------*\n")
                                            file.write(f"Receptionist Name :- {rname}\n")
                                            file.write(f"Receptionist Contact :- {rcontact}\n")                             
                                            file.write(f"Receptionist Age :- {rage}\n")                                 
                                            file.write(f"Receptionist Email :- {remail}\n")                                   
                                            file.write(f"Receptionist Address :- {raddress}\n")                               
                                            file.write(f"Receptionist Password :- {rpassword}\n")
                                            file.write(f"\n*--------------*------ Your Information End MR/Mrs.{rname} ---------*----------------*\n")
                                        
                                            
                                        print("\n------------------------ SuccessFully Receptionist Data Created ------------------------\n")
                                        break
                                    
                                    else:
                                        print("\n------------------------ Your Account Already Exists ------------------------")

                                else:
                                    print(f"************ {check_receptionist} ****************\n")
                                    
                            
                            
                            # Add Doctor Section  ..........# Done Full Validation
                            elif (add_account == "2"):
                                print("\n----------------------------------------- Add Doctor Section -----------------------------------------\n")
                                
                                while True:
                                    dname = input("Enter Doctor Name :")
                                    x = App.Doctor_NameValidation(dname)
                                    if x == True:  
                                        break
                                    else:
                                        print("\n----------------------- Invalid Name Format because Name also should be in String ---------------------- \n")


                                while True:
                                    dage = input("Enter Doctor Age :")
                                    x = App.Doctor_AgeValidation(dage)
                                    if x ==True:
                                        break
                                    else:
                                        print("\n----------------------- Invalid Name Format because Age also should be in Int ---------------------- \n")
                                
                                while True:
                                    demail = input("Enter Doctor Email :")
                                    x = App.Doctor_EmailValidation(demail)
                                    if x ==True:
                                        break
                                    else:
                                        print("\n----------------------- Invalid Name Format because Email also should be in Gmail Format ---------------------- \n")
                                    
                                dqualification = input("Enter Doctor Qualification :")
                                    
                                dspecilist = input("Enter Doctor Specification :")

                                dpassword = input("Enter Doctor Password :")

                                check_doctor = App.check_doctor_info(demail)
                                if check_doctor ==True:  
                                    d_account = App.D_CreateAccount(dname, dage, demail, dqualification, dspecilist, dpassword)
                                    if d_account ==True:
                                        # here print whole the Doctor data into the another folder name is Doctor 
                                        with open(f"Doctor-Data/{demail}.txt" , "a") as file:
                                            file.write("\n*-------------------This is Receptionist Information  ------------*-----------*\n")
                                            file.write(f"\n*--------------*-------Welcome to MR/Mrs .{dname}----------*-----------*----------*\n")
                                            file.write(f"Doctor  Name :- {dname}\n")
                                            file.write(f"Doctor Age  :- {dage}\n")                             
                                            file.write(f"Doctor Email :- {demail}\n")                                 
                                            file.write(f"Doctor Qualification :- {dqualification}\n")                                   
                                            file.write(f"Doctor Specialist :- {dspecilist}\n")                               
                                            file.write(f"Doctor Password :- {dpassword}\n")
                                            file.write(f"\n*--------------*------ Your Information End Mr/Mrs .{dname} ---------*----------------*\n")
                                        
                                        print("\n---------------------------  SuccessFully Doctor Account Created ---------------------------\n")
                                        break
                                    else:
                                        print("\n--------------------------- This Doctor Account is Already Exists So go Login -------------------------------\n")
                                else:
                                    print(f"\n-------------------------- {check_doctor} ----------------------------\n")       

                            # Add Patient Section ..........# Done Full Validation 
                            elif (add_account == "3"):
                                print("\n----------------------------------------- Add Patient Section -----------------------------------------\n")
                                while True:
                                    pname = input("Enter Patient Name :")
                                    x = App.Patient_NameValidation(pname)
                                    if x == True:  
                                        break
                                    else:
                                        print("\n----------------------- Invalid Name Format because Name also should be in String ---------------------- \n")
                                while True:
                                        pemail = input("Enter Patient Email :")
                                        x = App.Patient_EmailValidation(pemail)
                                        if x ==True:
                                            break
                                        else:
                                            print("\n----------------------- Invalid Name Format because Email also should be in Gmail Format ---------------------- \n")
                                while True:        
                                        page = input("Enter Paitent Age :")
                                        x = App.Patient_AgeValidation(page)
                                        if x == True:
                                            break
                                        else:
                                            print("-------invalid Age ---------")
                                while True:   
                                        pcontact = input("Enter Paitent Contact : ")
                                        x = App.Patient_ContactValidation(pcontact)
                                        if x == True:
                                            break
                                        else:
                                            print("------Invalid COntact Format ---------")
                                                
                                ptreatment = input("Enter Patient Treatment Type :")
                                ppassword = input("Enter Patient Password :")

                                check_patient = App.check_patient_info(pemail,pcontact)
                                if check_patient == True:

                                    p_account = App.P_CreateAccount( pname, pemail, page, pcontact,ptreatment, ppassword)
                                    if p_account == True:
                                        with open(f"Patient-Data/{pemail}.txt" , "a") as file:
                                            file.write("\n*-------------------This is Patient Information  ------------*-----------*\n")
                                            file.write(f"\n*--------------*-------Welcome to MR/Mrs .{pname}----------*-----------*----------*\n")
                                            file.write(f"Patient  Name :- {pname}\n")
                                            file.write(f"Patient Email  :- {pemail}\n")                             
                                            file.write(f"Patient Age :- {page}\n")                                 
                                            file.write(f"Patient Contact :- {pcontact}\n")                                   
                                            file.write(f"Patient Treatment  :- {ptreatment}\n")                               
                                            file.write(f"Patient Password :- {ppassword}\n")
                                            file.write(f"\n*--------------*------ Your Information End Mr/Mrs .{pname} ---------*----------------*\n")
                                        print("\n----------------------------------------- SuccessFully  Patient Account Created -----------------------------------------\n")                          
                                        break
                                    else:
                                        print("\n------------------------ Your Account Already Exists ------------------------")
                                else:
                                    # print(f"--------------------{check_patient}-------------------")
                                    print("\n------------------------ Your Account Already Exists ------------------------")
                                    
                            elif (add_account == "4"):
                                print("\n----------------------------------------- Thank You Create Account Section -----------------------------------------\n")
                                break
                            
                            else:
                                print("\n********************** Invalid Choice Section **********************\n")
                    

                    # Remove  Account .....# Done  Code
                    elif(ach =="4"):
                        while True:
                            print("\n----------------------------------------- Remove Accounts -----------------------------------------\n")
                            print("\n1- Receptionist Account \n2- Doctor Account \n3- Patient Account \n4- Exit \n")
                            remove_account = input("Enter Choice to Delete Account  :")

                            # remove receptionist acccount 
                            if (remove_account =="1"):
                            
                                print("\n\n----------------------------------------- Delete Receptinist Account -----------------------------------------\n")
                                remail  = input("Enter Email You want to Delete :")
                                dch = input("Are Your sure want to Delete Receptinist Account Account :(Y/N)")
                                if (dch =="Y" or dch =="yes" or "Yes" or "YES"):
                                    d = App.Delete_Receptionist(remail)
                                    print(f"\n********************** {d}***********************\n")

                            
                                else:

                                    print("\n********************* Process Has Been Cancelled ************************\n")

                            elif(remove_account =="2"):
                                print("\n----------------------------------------- Delete Doctor Account -----------------------------------------\n")
                                demail  = input("Enter Email You want to Delete :")
                                dch = input("Are Your sure want to Delete Receptinist Account Account :(Y/N)")
                                if (dch =="Y" or dch =="yes" or "Yes" or "YES"):
                                    d = App.Delete_Doctor(demail)
                                    print(f"\n********************* {d} *********************\n")

                            
                                else:

                                    print("\n------------------- Process Has Been Cancelled -------------------\n")

                            elif(remove_account =="3"):
                                print("\n----------------------------------------- Delete Patient Account -----------------------------------------\n")
                                pemail  = input("Enter Email You want to Delete :")
                                dch = input("Are Your sure want to Delete Receptinist Account Account :(Y/N)")
                                if (dch =="Y" or dch =="yes" or "Yes" or "YES"):
                                    d = App.Delete_Patient(pemail)
                                    print(f"\n********************* {d} ********************\n")

                            
                                else:

                                    print("********************** Process Has Been Cancelled ************************")

                            elif(remove_account =="4"):
                                print("\n------------------------------Thank You Delete Account Section  -------------------------------\n")
                                break
                            
                            else:
                                print("\n------------------------------Invalid Choice try , Again -------------------------------\n")
                        
                            
                    # view  the whole the account 
                    elif(ach == "5"):
                        while True:
                            print("\n----------------------------------------- View Account -----------------------------------------\n")
                            print("\n1-Receptionist \n2- Doctor \n3- Patient \n4- Exit \n")
                            view_account = input("Enter View Choice  Account : ")

                            if(view_account == "1"):
                                print("\n----------------------------------------- View Receptionist List -----------------------------------------\n")
                              
                                View_Receptionist = App.Show_ReceptionistInfo()
                                x = PrettyTable()
                                x.field_names = ["Receptionist  ID","Receptionist Name","Receptionist Contact","Receptionist Age","Receptionist Email","Receptionist Address","Receptionist Password"]
                                x.add_rows(View_Receptionist)
                                print(x)
                            
                            # view all the doctor who r present right now in the hosital  # Done Code
                            elif (view_account=="2"):
                                print("\n----------------------------------------- View All The  Doctors in The hospital -----------------------------------------\n")
                                
                                # a = (dname,dqualification,dspecilist)
                                view_doctor = App.Show_DoctorInfo()
                                x = PrettyTable()
                                x.field_names = ["Doctor ID","Doctor Name","Doctor Age","Doctor Email","Doctor Qualification","Doctor Specialist","Doctor Password"]
                                x.add_rows(view_doctor)
                                print(x)

                            #  view all the patient who r registered there information  # Done Code 
                            elif (view_account=="3"):
                                print("\n----------------------------------------- View All The Patients  in The hospital -----------------------------------------\n")
                              
                                # a = (dname,dqualification,dspecilist)
                                view_patient = App.Show_PatientInfo()
                                x = PrettyTable()
                                x.field_names = ["Patient ID","Patient Name","Patient Email ","Patient Age","Patient Contact","Patient TreatMent Type","Patient Password"]
                                x.add_rows(view_patient)
                                print(x)

                            elif(view_account=="4"):
                                print("\n----------------------------------------- Thank You View Section -----------------------------------------\n")
                                break
                            else:
                                print("\n----------------------------------------- Invalid Account View Choice , try Again -----------------------------------------\n")

                            
                    # Add Appointment Section .......# Done  Code
                    elif(ach =="6"):
                        print("\n----------------------------------------- Add Appointment Section -----------------------------------------\n")
                        print("\n1- Add Appointment \n2- View Appointment \n3- Delete Appointment \n4-Exit\n")
                        appoint_choice = input("Enter Appointment Choice :")
                        print("\n----------------------------------------- Add Appointment By Admin Section -----------------------------------------\n")
                        #check treatment is available or not
                        # book the appointment by admin     #pending check doctor, and patient , treatment avaialable or not 
                        if (appoint_choice =="1"):
                            #check treatment is available or not 
                            while True:
                                appoint_for = input("Enter Your TreatMent CHoice  :")
                                x = App.check_treatment_type(appoint_for)
                                if x !=None:
                                    break
                                else:
                                    print(f"\n-------------------This {appoint_for} Type Treatment  Not Available in The Hospital --------------------\n")
                                
                                #check appint_for doctors are available or not 
                            while True:
                                doctor_name = input("Enter Doctor Name :")
                                x = App.check_doctor_available(doctor_name)
                                if x != None:
                                    break
                                else:
                                    print(f"--------------------------------- This doctor {doctor_name} is not available in the Hosptial -------------------")
                        
                            while True:
                                patient_name = input("Enter Patient Name :")
                                x = App.check_patient_matched(patient_name)
                                if x != None:
                                    break
                                else:
                                    print(f"\n------------------ This {patient_name} Patient is not registered in the Hospital Yet --------------------\n")

                                #check appint_for are available or not 
                            identity = ("Admin")
                            t = time.strftime("%d,%m,%Y")
                            
                            x = App.Book_Appointment(appoint_for,doctor_name,patient_name,a_username,identity)
                            
                            # here print whole the Appointment data into the another folder name is Appointment 
                            with open(f"Appointment-Data/{patient_name}.txt" , "a") as file:
                                file.write("\n*-------------------This is Appointment Information  ------------*-----------*\n")
                                file.write(f"\n*--------------*-------Welcome to MR/Mrs .{patient_name}----------*-----------*----------*\n")
                                file.write(f"Appointment For :- {appoint_for}\n")                           
                                file.write(f"Doctor Name  :- {doctor_name}\n")                                 
                                file.write(f"Patient Name :- {patient_name}\n")                                   
                                file.write(f"Appointment identity :- {identity}\n")                               
                                file.write(f"Appointment DateTime :- {t}\n")
                                file.write(f"\n*--------------*------ Your Information{patient_name} ---------*----------------*\n")
                                
                            print(f"\n--------------------------------- SuccessFully Paitent Appointment Booked : {t} -----------------------------------\n")
                        
                        # view all the appointment record 
                        elif(appoint_choice=="2"):
                            print("\n--------------------- View All The Appointment Data -----------------------\n")
                            view_appoint =  App.View_Appointment()
                            x = PrettyTable()
                            x.field_names = ["Apppintment Number","Appointment For","Doctor Name","Patient Name","identity","Book By","Appointment Date"]
                            x.add_rows(view_appoint)
                            print(x)
                        
                        # delete the particular appointment data in sql 
                        elif(appoint_choice=="3"):
                            print("\n-------------------------------- Delete Appointment ------------------------------------------\n")
                            
                            appointment_id  = input("Enter Appointment ID  You want to Delete :")
                            dch = input("Are Your sure want to Delete Appointment  Account :(Y/N)")
                            if (dch =="Y" or dch =="yes" or "Yes" or "YES"):
                                d = App.Delete_Appointment(appointment_id)
                                print(f"\n********************** {d}***********************\n")

                                
                            else:

                                print("\n********************* Process Has Been Cancelled ************************\n")

                    
                        else:
                            print("\n----------------------------- Thank You Receptionist Section --------------------------------------\n")

                    elif (ach == "7"):
                        print("\n----------------------------------------- Thank You Admin Section -----------------------------------------\n")
                        break

                    else:
                        print("\n----------------------------------------- Invalid Admin Choice -----------------------------------------\n")

    # Receptionist Login ........ # Done Login Code  ,  #Pending REgx
    elif (ch == "2"):
        print("\n----------------------------------------- Receptionist Login Section -----------------------------------------\n")
        # here start receptionist working  # Done # Validation  login
        while True:
            remail = input("Enter Your Email - ID : ")
            x = App.Receptionist_EmailValidation(remail)
            if x == True:
                break
            else:
                print("---------Invalid Email Address-------------")

        rpassword = input("Enter Your Password : ")
        R = App.Receptionist_Login(remail, rpassword)
        s = ("Receptionist")
        ti =time.strftime("%Y-%m-%d %H:%M")
        if R == None:
            print("\n----------------------------------------- InCorrect Receptionist Account -----------------------------------------\n")
        else:
            print("\n----------------------------------------- SuccessFully Receptionist Logged In -----------------------------------------\n")
            print(f"Hello {s} Welcome to  Hospital {ti}")
            while True:
                print("\n----------------------------------------- Receptionist Section -----------------------------------------\n")
                print("\n1- Our Profile \n2-  Doctor Accounts  \n3- Patient Accounts  \n4- Add Appointment  \n5- View Appoinments \n6-Update Receptionist Info \n7-Exit\n")
                r_choice = input("Enter Recepionist Choice : ")

                #view Receptionist Profile ......   #  Done Code 
                if(r_choice=="1"):
                    print("\n----------------------------------------- View Admin  Profile -----------------------------------------\n")
                    
                    View_Receptionist = App.ReceptionistProfile(remail)
                    x = PrettyTable()
                    x.field_names = ["ID"," Name"," Contact"," Age"," Email"," Address"," Password"]
                    x.add_row(View_Receptionist)
                    print(x)
                    
                # view all the doctor who r present  in the hosital  # Done Code
                elif(r_choice =="2"):
                    print("\n----------------------------------------- View All The  Doctor Information -----------------------------------------\n")
                    view_doctor = App.Show_DoctorInfo()
                    x = PrettyTable()
                    x.field_names = ["Doctor ID","Doctor Name","Doctor Age","Doctor Email","Doctor Qualification","Doctor Specialist","Doctor Password"]
                    x.add_rows(view_doctor)
                    print(x)
                # Patient information code here 
                elif(r_choice =="3"):
                    print("\n-------------------------------------Patients Details Section ----------------------------------------\n")
                    print("\n1- Add Patient \n2- View Patient \n3- Exit\n")
                    patient_ch = input("Enter Patient Info Choice : ")

                    #  add the patient account here 
                    if(patient_ch =="1"):
                        print("\n----------------------------------------- Add Patient Section -----------------------------------------\n")
                        while True:
                            pname = input("Enter Patient Name :")
                            x = App.Patient_NameValidation(pname)
                            if x == True:  
                                break
                            else:
                                print("\n----------------------- Invalid Name Format because Name also should be in String ---------------------- \n")
                        while True:
                                pemail = input("Enter Patient Email :")
                                x = App.Patient_EmailValidation(pemail)
                                if x ==True:
                                    break
                                else:
                                    print("\n----------------------- Invalid Name Format because Email also should be in Gmail Format ---------------------- \n")
                        while True:        
                                page = input("Enter Paitent Age :")
                                x = App.Patient_AgeValidation(page)
                                if x == True:
                                    break
                                else:
                                    print("-------invalid Age ---------")
                        while True:   
                                pcontact = input("Enter Paitent Contact : ")
                                x = App.Patient_ContactValidation(pcontact)
                                if x == True:
                                    break
                                else:
                                    print("------Invalid COntact Format ---------")
                                        
                        ptreatment = input("Enter Patient Treatment Type :")
                        ppassword = input("Enter Patient Password :")

                        check_patient = App.check_patient_info(pemail,pcontact)
                        if check_patient == True:

                            p_account = App.P_CreateAccount( pname, pemail, page, pcontact,ptreatment, ppassword)
                            if p_account == True:
                                with open(f"Patient-Data/{pname}.txt" , "a") as file:
                                    file.write("\n*-------------------This is Patient Information  ------------*-----------*\n")
                                    file.write(f"\n*--------------*-------Welcome to MR/Mrs .{pname}----------*-----------*----------*\n")
                                    file.write(f"Patient  Name :- {pname}\n")
                                    file.write(f"Patient Email  :- {pemail}\n")                             
                                    file.write(f"Patient Age :- {page}\n")                                 
                                    file.write(f"Patient Contact :- {pcontact}\n")                                   
                                    file.write(f"Patient Treatment  :- {ptreatment}\n")                               
                                    file.write(f"Patient Password :- {ppassword}\n")
                                    file.write(f"\n*--------------*------ Your Information End Mr/Mrs .{pname} ---------*----------------*\n")
                                print("\n----------------------------------------- SuccessFully  Patient Account Created -----------------------------------------\n")                          
                                break
                            else:
                                print("\n------------------------ Your Account Already Exists ------------------------")
                        else:
                            # print(f"--------------------{check_patient}-------------------")
                            print("\n------------------------ Your Account Already Exists ------------------------")


                    # View all the patient account here .....
                    elif(patient_ch =="2"):
                        print("----------------------------------------- View  Patient  Account -----------------------------------------\n")
                        view_patient = App.Show_PatientInfo()
                        x = PrettyTable()
                        x.field_names = ["Patient ID","Patient Name","Patient Email ","Patient Age","Patient Contact","Patient TreatMent Type","Patient Password"]
                        x.add_rows(view_patient)
                        print(x)
                    
                    elif(patient_ch =="3"):
                        print("----------------------------------------- Thank You Patient  Account Section -----------------------------------------\n")
                        break
                    else:
                        print("\n-----------------------------------------Invalid Patient Info Choice -----------------------------------------\n")

                # Book Appointment With Patient Information and Doctor Information   # Done Code 
                elif (r_choice=="4"):
                    print("\n----------------------------------------- Add Appointment By Receptionist Section -----------------------------------------\n")
                    #check treatment is available or not 
                    while True:
                        appoint_for = input("Enter Your Treatment CHoice  :")
                        x = App.check_treatment_type(appoint_for)
                        if x !=None:
                            break
                        else:
                            print(f"\n-------------------This {appoint_for} Type Treatment  Not Available in The Hospital --------------------\n")
                    while True:    
                        doctor_name = input("Enter Doctor Name :")
                        
                        x = App.check_doctor_available(doctor_name)
                        if x != None:
                            break
                        else:
                            print(f"--------------------------------- This doctor {doctor_name} is not available in the Hosptial -------------------")
                    while True:
                        patient_name = input("Enter Patient Name :")
                        x = App.check_patient_matched(patient_name)
                        if x != None:
                            break
                        else:
                            print(f"\n------------------ This {patient_name} Patient is not registered in the Hospital Yet --------------------\n")

                    identity = ("Receptionist")
                    t = time.strftime("%d,%m,%Y")
                    C = (appoint_for,doctor_name,patient_name)
                    if C == None:
                        print("----------- These all Wrong Details ------------")
                       

                        
                    App.Book_Appointment(appoint_for,doctor_name,patient_name,remail,identity)
                     # here print whole the Appointment data into the another folder name is Appointment 
                    with open(f"Appointment-Data/{patient_name}.txt" , "a") as file:
                        file.write("\n*-------------------This is Appointment Information  ------------*-----------*\n")
                        file.write(f"\n*--------------*-------Welcome to MR/Mrs .{patient_name}----------*-----------*----------*\n")
                        file.write(f"Appointment For :- {appoint_for}\n")                           
                        file.write(f"Doctor Name  :- {doctor_name}\n")                                 
                        file.write(f"Patient Name :- {patient_name}\n")                                   
                        file.write(f"Appointment identity :- {identity}\n")                               
                        file.write(f"Appointment DateTime :- {t}\n")
                        file.write(f"\n*--------------*------ Your Information{patient_name} ---------*----------------*\n")
                        
                    print(f"\n--------------------------------- SuccessFully Paitent Appointment Booked : {t} -----------------------------------\n")
                    
                
                       
                # View All The Appointments ......
                elif (r_choice=="5"):
                    print("\n----------------------------------------- View  Appointment Section -----------------------------------------\n")
                    #
                    view_appoint =  App.View_Appointment()
                    x = PrettyTable()
                    x.field_names = ["Apppintment Number","Appointment For","Doctor Name","Patient Name","identity","Book By","Appointment Date"]
                    x.add_rows(view_appoint)
                    print(x)

                    
                
                # UpDate Receptionist Information ........... Done Code 
                elif(r_choice =="6"):
                    print("\n----------------------------------------- Update Receptionist Section -----------------------------------------\n")
                    while True:
                        print("\n1- Update Name \n2- Update Age \n3- Update Email  & Address \n4- Update Password \n5-Exit \n")
                       
                        r_update = input("Enter Your  Update Choice :")
                        
                        # update receptionist name only   
                        if(r_update =="1"):
                            print("\n----------------------------------------- Update Name -----------------------------------------\n")
                            new_name = input("Enter Receptionist New Name :")
                            App.UpdateReceptionist(new_name, remail)
                            print("\n----------------------------------------- SuccesssFylly Updated -----------------------------------------\n")
                        
                        # update receptionist age only    
                        elif (r_update =="2"):
                            print("\n----------------------------------------- Update Age -----------------------------------------\n")
                            new_age = int(input("Enter Receptionist New Age : "))
                            App.UpdateReceptionist(new_age,remail)
                            print("\n-----------------------------------------  SuccessFully Age Updated -----------------------------------------\n")
                            
                        
                        # update receptionist Email & Address  only  
                        elif(r_update=="3"):
                            print("\n----------------------------------------- Update Email & Address -----------------------------------------\n")
                            new_email = input("Enter New Receptionist Email :")
                            new_address = input("Enter New Receptionist Address :")
                            App.UpdateReceptionist(new_email,new_address,remail)
                            print("\n----------------------------------------- SuccessFully Updated Eamil & Address -----------------------------------------\n")
                        
                        # update receptionist Password  only  
                        elif(r_update =="4"):
                            print("\n----------------------------------------- Update Password -----------------------------------------\n")
                            new_password = input("Enter New Receptionist Password :")
                            App.UpdateReceptionist(new_password,remail)
                            print("\n----------------------------------------- Successfully Updated Password -----------------------------------------\n")
                        
                        # update receptionist age only  
                        elif(r_update=="5"):
                            print("\n----------------------------------------- Thank You Update Section -----------------------------------------\n")
                            break
                        else:
                            print("\n----------------------------------------- Invalid Choice -----------------------------------------\n")

                
                elif (r_choice=="7"):
                    print("\n----------------------------------------- Thank You Receptionist Section -----------------------------------------\n")
                    break
                else:
                    print("\n----------------------------------------- Invalid Syntax -----------------------------------------\n")       

    # Doctor Login............... # Done Login Code #Pending REgx
    elif (ch == "3"):
        print("\n----------------------------------------- Doctor Login Section -----------------------------------------\n")
        # check doctor login section ................
        demail = input("Enter Your Email - ID : ")
        dpassword = input("Enter Your Password : ")
        R = App.Doctor_Login(demail, dpassword)
        s = ("Doctor")
        ti =time.strftime("%Y-%m-%d %H:%M")
        if R == None:
            print("\n----------------------------------------- InCorrect Doctor Password -----------------------------------------\n")
        
        else:
            print("\n----------------------------------------- SuccessFully Doctor Logged In -----------------------------------------\n")
            print(f"Hello {s} Welcome to  Hospital {ti}")
            # here start doctor perform different -2 task 
            while True:
                print("\n----------------------------------------- Doctor Section -----------------------------------------\n")
                print("\n1- Our Profile \n2- View Patient  \n3- View Appoinment \n4- Update Doctor Info \n5- Exit \n")
                d_choice = input("Enter Doctor CHoice : ")
                
                # View Our Profile ..............
                if(d_choice =="1"):
                    print("\n----------------------------------------- View Doctor  Profile -----------------------------------------\n")
                    
                    View_doctor = App.DoctorProfile(demail)
                    x = PrettyTable()
                    x.field_names = ["ID"," Name"," Age"," Email"," Qualification","Specialist"," Password"]
                    x.add_row(View_doctor)
                    print(x)
                # View All the Patient List  this method call to Patient class  # Done Code
                elif(d_choice =="2"):
                    print("\n----------------------------------------- View All The Patient -----------------------------------------\n")
                    view_patient = App.Patient_History()
                    x = PrettyTable()
                    x.field_names = ["Patient Name","Patient Age","Patient Contact","Patient TreatMent Type "]
                    x.add_rows(view_patient)
                    print(x)

                #View All The Appointment where patient appointed to particular doctor name  # Done Code 
                elif(d_choice =="3"):
                    print(f"\n------------------------------ View All The Patient Appointent to {demail} ----------------------------------------\n")
                    try:
                        # view_appoint = App.Appointment_Alocate_Doctor(demail,)
                        view_appoint = App.Appointment_Alocate_Doctor(demail)
                        # print(view_appoint)
                        x = PrettyTable()
                        x.field_names = ["appointment_id"," appointment_for"," Doctor_name"," Patient_name"," identity","Book_By "," Apppintment_date"]
                        x.add_rows(view_appoint)
                        print(x)
                    except:
                        print("You have to no any Appointted Patient")

                # Update Doctor INfo   #  Done Code 
                elif(d_choice =="4"):
                    while True:
                        print("\n----------------------------------------- Doctor Update Section -----------------------------------------\n")
                        
                        print("\n1- Update Doctor Name \n2-Update Doctor Age \n3-Update Doctor Email \n4- Update Doctor Qualification & Specialist \n5-Update Doctor Password \n6-Exit  \n")
                        
                        d_update = input("Enter Doctor Update Choice :")
                        
                        #Update Doctor Name ..........
                        if(d_update =="1"):
                            print("\n----------------------------------------- Doctor Name Update Section -----------------------------------------\n")
                            
                            new_name = input("Enter Doctor New Name :")
                            App.UpdateDoctor(new_name,demail)
                            print("\n----------------------------------------- SUccessFully Update Name -----------------------------------------\n")


                        #Update Doctor Age  ..........
                        elif(d_update=="2"):
                            print("\n----------------------------------------- Doctor Age Update Section -----------------------------------------\n")
                            
                            new_age = int(input("Enter Doctor New Age :"))
                            App.UpdateDoctor(new_age,demail)
                            print("\n----------------------------------------- SUccessFully Update Age -----------------------------------------\n")

                            #Update Doctor Email  ..........
                        elif(d_update=="3"):
                            print("\n----------------------------------------- Doctor Email Update Section -----------------------------------------\n")
                            
                            new_email = input("Enter Doctor New Email :")
                            App.UpdateDoctor(new_email,demail)
                            print("\n----------------------------------------- SUccessFully Update Email -----------------------------------------\n")


                            #Update Doctor Qualification & Specilist  ..........
                        elif(d_update=="4"):
                            print("\n----------------------------------------- Doctor Email Qualification & Specilist Section -----------------------------------------\n")
                            
                            new_qualification = input("Enter Doctor New Qualification :")
                            new_specialist = input("Enter Doctor New Specilist : ")
                            App.UpdateDoctor(new_qualification,new_specialist,demail)
                            print("\n----------------------------------------- SUccessFully Update Doctor Qualification & Specilist -----------------------------------------\n")

                            #Update Doctor Password ..........
                        elif(d_update=="5"):
                            print("\n----------------------------------------- Doctor Email Update Section -----------------------------------------\n")
                            
                            new_password = input("Enter Doctor New Password :")
                            
                            App.UpdateDoctor(new_password,demail)
                            print("\n----------------------------------------- SUccessFully Update Doctor Password -----------------------------------------\n")

                        elif(d_update=="6"):
                            print("\n----------------------------------------- Thank You Doctor Update Section -----------------------------------------\n")
                            break
                        else:
                            print("\n----------------------------------------- Invalid Update Choice -----------------------------------------\n")


                
                elif(d_choice =="5"):
                    print("\n----------------------------------------- Thank You Doctor Section -----------------------------------------\n")
                    break
                
                else:
                    print("\n----------------------------------------- Invalid Syntax -----------------------------------------\n")

    # Patient Login.............. # Done Login Code #Pending REgx
    elif (ch == "4"):
        print("\n----------------------------------------- Doctor Login Section -----------------------------------------\n")

        pemail = input("Enter Your Email - ID : ")
        ppassword = input("Enter Your Password : ")
        P = App.Patient_Login(pemail, ppassword)
        s = ("Patient")
        ti =time.strftime("%Y-%m-%d %H:%M")
        if P == None:
            print("\n----------------------------------------- InCorrect Patient Password -----------------------------------------\n")
        else:
            print("\n----------------------------------------- SuccessFully Patient Logged In -----------------------------------------\n")
            print(f"Hello {s} Welcome to Hospital {ti}")
            # here start whole the code for patient operations  # Pending
            while True:
                print("\n----------------------------------------- Patient Section-----------------------------------------\n")
                print("\n1-Our Profile \n2- View Doctor \n3- View Your Appointment \n4- Apply An  Appointment \n5- Update Patient Info \n6- Exit \n")
                
                p_choice = input("Enter Your Choice : ")

                # Patient Profile ..............
                if(p_choice =="1"):
                    print("\n----------------------------------------- View Doctor  Profile -----------------------------------------\n")
                    
                    View_patient = App.PatientProfile(pemail)
                    x = PrettyTable()
                    x.field_names = ["ID"," Name"," Email"," Age"," Contact","TreatMent "," Password"]
                    x.add_row(View_patient)
                    print(x)


                    # view the all doctord  from call to admin class   # Done Code

                elif (p_choice=="2"):
                    # while True:
                        print("\n----------------------------------------- TreatMent Type -----------------------------------------\n")
                        print("\n1- Skin \n2- Adult \n3- Child \n4- Body \n5- Women Specilist \n6- ENT Specialist \n7- Exit \n")
                        
                        treatment = input("Enter Treatment Choice : ")

                        if (treatment =="1"):
                            print("\n----------------------------------------- Skin Treatments Type Doctor here-----------------------------------------\n")
                            view_doctor = App.Skin_Doctor()
                            x = PrettyTable()
                            x.field_names = ["Doctor Name","Doctor Qualification","Doctor Specialist"]
                            x.add_rows(view_doctor)
                            print(x)

                        elif(treatment =="2"):
                            print("\n----------------------------------------- Adult Treatments Type Doctor here -----------------------------------------\n")
                            view_doctor = App.Adult_Doctor()
                            x = PrettyTable()
                            x.field_names = ["Doctor Name","Doctor Qualification","Doctor Specialist"]
                            x.add_rows(view_doctor)
                            print(x)

                        elif(treatment=="3"):
                            print("\n----------------------------------------- Child Treatments Type Doctor here -----------------------------------------\n")
                            view_doctor = App.Child_Doctor()
                            x = PrettyTable()
                            x.field_names = ["Doctor Name","Doctor Qualification","Doctor Specialist"]
                            x.add_rows(view_doctor)
                            print(x)

                        elif(treatment=="4"):
                            print("\n----------------------------------------- Body Treatments Type Doctor here-----------------------------------------\n")
                            view_doctor = App.Body_Doctor()
                            x = PrettyTable()
                            x.field_names = ["Doctor Name","Doctor Qualification","Doctor Specialist"]
                            x.add_rows(view_doctor)
                            print(x)

                        elif(treatment=="5"):
                            print("\n----------------------------------------- Women Specilist Treatments Type Doctor here -----------------------------------------\n")
                            view_doctor = App.Women_Doctor()
                            x = PrettyTable()
                            x.field_names = ["Doctor Name","Doctor Qualification","Doctor Specialist"]
                            x.add_rows(view_doctor)
                            print(x)

                        elif(treatment=="6"):
                            print("\n----------------------------------------- ENT Specialist Treatments Type Doctor here ----------------")
                            view_doctor = App.ENT_Doctor()
                            x = PrettyTable()
                            x.field_names = ["Doctor Name","Doctor Qualification","Doctor Specialist"]
                            x.add_rows(view_doctor)
                            print(x)
                        elif(treatment=="7"):
                            print("\n----------------------------------------- Thank You Treatment Type Section -----------------------------------------\n")
                            break

                        else:
                            print("\n----------------------------------------- Invalid Choice -----------------------------------------\n")

                # View your Appointment     # Done Code 
                elif (p_choice =="3"):
                    print("\n------------------------ Patient Appointment Section -------------------------------\n")
                    # appointment_id | appointment_for | Doctor_name | Patient_name | identity             | Book_By      | Apppintment_date 
                    try:
                        view_appoint = App.Appointment_Alocated_Patient(pemail,)
                        x = PrettyTable()
                        x.field_names = ["appointment_id"," appointment_for"," Doctor_name"," Patient_name"," identity","Book_By "," Apppintment_date"]
                        x.add_rows(view_appoint)
                        print(x)
                    except :
                        print("First Book Your Appointment then View Appointment")
                
                    
                # Apply Apppintment    # Done  Code
                elif(p_choice =="4"):
                    print("\n----------------------------------------- Add Appointment By Patient Section -----------------------------------------\n")
                    while True:
                        appoint_for = input("Enter Your Treatment CHoice  :")
                        x = App.check_treatment_type(appoint_for)
                        if x !=None:
                            break
                        else:
                            print(f"\n-------------------This {appoint_for} Type Treatment  Not Available in The Hospital --------------------\n")
                    while True:  
                        doctor_name = input("Enter Doctor Name :")

                        x = App.check_doctor_available(doctor_name)
                        if x != None:
                            break
                        else:
                            print(f"--------------------------------- This doctor {doctor_name} is not available in the Hosptial -------------------")
                    while True:
                        patient_name = input("Enter Patient Name :")
                        x = App.check_patient_matched(patient_name)
                        if x != None:
                            break
                        else:
                            print(f"\n------------------ This {patient_name} Patient is not registered in the Hospital Yet --------------------\n")

                    identity = ("Patient")
                    t = time.strftime("%d,%m,%Y")
                    App.Book_Appointment(appoint_for,doctor_name,patient_name,pemail,identity)
                        # here print whole the Appointment data into the another folder name is Appointment 
                    with open(f"Appointment-Data/{patient_name}.txt" , "a") as file:
                        file.write("\n*-------------------This is Appointment Information  ------------*-----------*\n")
                        file.write(f"\n*--------------*-------Welcome to MR/Mrs .{patient_name}----------*-----------*----------*\n")
                        file.write(f"Appointment For :- {appoint_for}\n")                           
                        file.write(f"Doctor Name  :- {doctor_name}\n")                                 
                        file.write(f"Patient Name :- {patient_name}\n")                                   
                        file.write(f"Appointment identity :- {identity}\n")                               
                        file.write(f"Appointment DateTime :- {t}\n")
                        file.write(f"\n*--------------*------ Your Information{patient_name} ---------*----------------*\n")
                        
                    print(f"\n--------------------------------- SuccessFully Paitent Appointment Booked : {t} -----------------------------------\n")
                

                # Update Patient Info .......... #  Done Code 
                elif(p_choice =="5"):
                    print("\n----------------------------------------- Patient Update Section -----------------------------------------\n")
                    while True:
                            print("\n1- Update Patient Email \n2- Update Patient Contact \n3- Update Patient Password \n4- Update All Data \n5- Exit \n")
                            
                            p_update = input("Enter Patient Update CHpice : ")
                                        
                            # Update Patient Email         #  Done Code 
                            if(p_update =="1"):
                                print("\n----------------------------------------- Patient Update Email  Section -----------------------------------------\n")
                                new_email = input("Enter Patient New Email :")
                                App.UpdatePatient(new_email,pemail)
                                print("\n----------------------------------------- SuccessFully Patient Name Update -----------------------------------------\n")

                            #Update patient Contact      #  Done Code 
                            elif(p_update =="2"):
                                print("\n----------------------------------------- Patient Update Contact Section -----------------------------------------\n")
                                new_contact = input("Enter Patient New Contact  :")
                                App.UpdatePatient(new_contact,pemail)
                                print("\n----------------------------------------- SuccessFully Patient Contact Update -----------------------------------------\n")

                            # Update Patient Password        #  Done Code 
                            elif(p_update =="3"):
                                print("\n----------------------------------------- Patient Update Password -----------------------------------------\n")
                                new_password = input("Enter Patient New Password :")
                                App.UpdatePatient(new_password,pemail)
                                print("\n----------------------------------------- SuccessFully Patient Password Update -----------------------------------------\n")
                                    
                                # Update patient WHole The Details          #  Done Code 
                            elif(p_update =="4"):
                                print("\n----------------------------------------- Update Whole The Patinet Information -----------------------------------------\n")
                                new_email = input("Enter Patient New Email :")
                                new_contact = input("Enter Patient New Contact  :")
                                new_password = input("Enter Patient New Password :")
                                App.UpdatePatient(new_email,new_contact,new_password,pemail)
                                        
                            elif(p_update =="5"):
                                    print("\n----------------------------------------- Thank You Patient Update Section -----------------------------------------\n")
                                    break
                            else:
                                print("\n----------------------------------------- Invalid Patient Update Choice -----------------------------------------\n")


                elif(p_choice =="6"):
                    print("\n----------------------------------------- Thank You Paitent Section -----------------------------------------\n")
                    break
                else:
                    print("\n----------------------------------------- Invalid Syntax -----------------------------------------\n")              

                
    # Print all the  specialist doctors.............. Done View code
    elif (ch == "5"):
        # while True:
            print("\n----------------------------------------- TreatMent Type  -----------------------------------------\n")
            print("\n1- Skin \n2- Adult \n3- Child \n4- Body \n5- Women Specilist \n6- ENT Specialist \n7- Exit \n")
           
            treatment = input("Enter Treatment Choice : ")
            try:
                if (treatment =="1"):
                    print("\n----------------------------------------- Skin Treatments Type Doctor here -----------------------------------------\n")
                    view_doctor = App.Skin_Doctor()
                    x = PrettyTable()
                    x.field_names = ["Doctor Name","Doctor Qualification","Doctor Specialist"]
                    x.add_rows(view_doctor)
                    print(x)

                elif(treatment =="2"):
                    print("\n----------------------------------------- Adult Treatments Type Doctor here -----------------------------------------\n")
                    view_doctor = App.Adult_Doctor()
                    x = PrettyTable()
                    x.field_names = ["Doctor Name","Doctor Qualification","Doctor Specialist"]
                    x.add_rows(view_doctor)
                    print(x)

                elif(treatment=="3"):
                    print("\n----------------------------------------- Child Treatments Type Doctor here -----------------------------------------\n")
                    view_doctor = App.Child_Doctor()
                    x = PrettyTable()
                    x.field_names = ["Doctor Name","Doctor Qualification","Doctor Specialist"]
                    x.add_rows(view_doctor)
                    print(x)

                elif(treatment=="4"):
                    print("\n----------------------------------------- Body Treatments Type Doctor here -----------------------------------------\n")
                    view_doctor = App.Body_Doctor()
                    x = PrettyTable()
                    x.field_names = ["Doctor Name","Doctor Qualification","Doctor Specialist"]
                    x.add_rows(view_doctor)
                    print(x)

                elif(treatment=="5"):
                    print("\n----------------------------------------- Women Specilist Treatments Type Doctor here -----------------------------------------\n")
                    view_doctor = App.Women_Doctor()
                    x = PrettyTable()
                    x.field_names = ["Doctor Name","Doctor Qualification","Doctor Specialist"]
                    x.add_rows(view_doctor)
                    print(x)

                elif(treatment=="6"):
                    print("\n----------------------------------------- ENT Specialist Treatments Type Doctor here -----------------------------------------\n")
                    view_doctor = App.ENT_Doctor()
                    x = PrettyTable()
                    x.field_names = ["Doctor Name","Doctor Qualification","Doctor Specialist"]
                    x.add_rows(view_doctor)
                    print(x)
                
                elif(treatment=="7"):
                    print("\n----------------------------------------- Thank You Treatment Type Section -----------------------------------------\n")
                    break
            

                else:
                    print("\n----------------------------------------- Invalid Choice -----------------------------------------\n")
            except:
                print("\n----------------------------------------- Invalid Choice -----------------------------------------\n")
            finally:
                print("\n----------------------------------------------------------------------------------------------------------------\n")
                print("  You are First time visiting in the Hospital so If You Want to Book Your Appointment then Contact to Receptionist ")
                print("\n-------------------------------------------------------------------------------------------------------------------\n")
               
    # Exit The Software 
    elif (ch == "6"):
        print("\n----------------------------------------- Thank You -----------------------------------------\n")
        break
    
    else:
        print("\n----------------------------------------- Invalid Syntax -----------------------------------------\n")

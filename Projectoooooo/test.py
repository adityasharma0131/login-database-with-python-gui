from tkinter import *
import customtkinter
# import mian
import mysql.connector
import os
import math
import random
import smtplib

root = customtkinter.CTk()
root.title("Login")
root.geometry("1000x600")
customtkinter.set_appearance_mode("dark")
root.resizable(False, False)
root.iconbitmap("logo1.ico")


hide_img = PhotoImage(file = "icons8-hide-24.png")
show_img = PhotoImage(file = "icons8-eye-24.png")

db_connect = mysql.connector.connect(
            host='localhost',
            user ='root',
            port='3306',
            password='',
            database='login_dbms');

mycursor = db_connect.cursor();

##############################################################

def Register(Full_Name,User_Name,Email_id,Password ):
    
    Full_name = Full_Name.get()
    User_name = User_Name.get()
    Email_id = Email_id.get()
    Password = Password.get()

    insertion = "INSERT INTO login_Data values(%s,%s,%s,%s)"
    val_insertion = (Full_name, User_name, Email_id, Password)

    mycursor.execute(insertion, val_insertion)
    db_connect.commit()
    Sign_IN()



def changeYour_psswd():
    def on_enter(e):
        Change_psswd['bg'] = '#fff'
        Change_psswd['fg'] = '#000'

    def on_leave(e):
        Change_psswd['bg'] = '#242424'
        Change_psswd['fg'] = '#9e9e9e'
        
    def on_enterr(e):
        cancelBttn['bg'] = '#fff'
        cancelBttn['fg'] = '#000'

    def on_leaver(e):
        cancelBttn['bg'] = '#242424'
        cancelBttn['fg'] = '#9e9e9e'
    
    def show_psswd():
            confirm_Password.configure(show = "")
            hidePSSWD_button = Button(master=confirm_Password, image=hide_img ,bg="#343638", borderwidth=0, command=hide_psswd)
            hidePSSWD_button.place(x = 390, y = 14)
                
    def hide_psswd():
        confirm_Password.configure(show = "*")
        showPSSWD_button = Button(master=confirm_Password, image=show_img ,bg="#343638", borderwidth=0, command=show_psswd)
        showPSSWD_button.place(x = 390, y = 14) 

        
    frame = customtkinter.CTkFrame(root, width=430, height = 550, bg_color="#242424", corner_radius = 20 )
    frame.place(x = 530, y = 30)    

    heading = Label(frame,fg="#fff",bg="#2b2b2b",  text="Reset Password" ,font=('Century Gothic',28, 'bold'))
    heading.place(x=120,y=10)

    new_Password = customtkinter.CTkEntry(frame, width=350, height = 45 ,placeholder_text="New Password", font=('Rod',15,'bold'), show="*")
    new_Password.place(x=30, y=80)
        
    confirm_Password = customtkinter.CTkEntry(frame, width=350, height = 45 , placeholder_text="Confirm New Password", font=('Rod',15,'bold'), show="*")
    confirm_Password.place(x=30, y=150)
    
    # OTp_sys = customtkinter.CTkEntry(frame, width=350, height = 45 , placeholder_text="OTP", font=('Rod',15,'bold'))
    # OTp_sys.place(x=30, y=220)
    
    showPSSWD_button = Button(master=confirm_Password, image=show_img,  bg="#343638", borderwidth=0, command=show_psswd)
    showPSSWD_button.place(x = 390, y = 14)
        
    # generate_OTP = Button(frame, text="generate OTP", border=0,  bg='#2b2b2b', fg="#9e9e9e", font=('Century Gothic',10), cursor='hand2', command= lambda: generate_OTP_sys(User_Name,Email,generate_OTP))
    # generate_OTP.bind("<Enter>", on_entero)
    # generate_OTP.bind("<Leave>", on_leaveo)
    # generate_OTP.place(x=365 ,y = 335)

        # new_Password = customtkinter.CTkEntry(frame, width=350,height = 45 , placeholder_text="New Password", font=('Rod',15,'bold'))
        # new_Password.place(x=30, y=220)

        # confirm_Password = customtkinter.CTkEntry(frame, width=350,height = 45 , placeholder_text="Confirm New Password", font=('Rod',15,'bold'), show="*")
        # confirm_Password.place(x=30, y=290)
        
        # def show_psswd():
        #     confirm_Password.configure(show = "")
        #     hidePSSWD_button = Button(master=confirm_Password, image=hide_img ,bg="#343638", borderwidth=0, command=hide_psswd)
        #     hidePSSWD_button.place(x = 390, y = 14)
                
        # def hide_psswd():
        #     confirm_Password.configure(show = "*")
        #     showPSSWD_button = Button(master=confirm_Password, image=show_img ,bg="#343638", borderwidth=0, command=show_psswd)
        #     showPSSWD_button.place(x = 390, y = 14)
    
    

    cancelBttn = Button(master=frame, borderwidth = 0, width=15, height = 2 , fg="#9e9e9e", text="Cancel", bg='#242424', font=('Rod',15,'bold'), command=lambda: Sign_IN())
    cancelBttn.bind("<Enter>", on_enterr)
    cancelBttn.bind("<Leave>", on_leaver)
    cancelBttn.place(x = 280, y = 385)
        
        
    Change_psswd = Button(master=frame, borderwidth = 0, width=17, height = 2 , fg="#9e9e9e", text="Confirm", bg='#242424', font=('Rod',15,'bold'), command=lambda: Forget_Auth(generate_OTP_sys.username,generate_OTP_sys.emailid,confirm_Password,Change_psswd,new_Password))
    Change_psswd.bind("<Enter>", on_enter)
    Change_psswd.bind("<Leave>", on_leave)
    Change_psswd.place(x = 43, y = 385)
    


def generate_OTP_sys(User_Name,Email,generate_OTP):
    
    generate_OTP_sys.username = User_Name.get()
    generate_OTP_sys.emailid = Email.get()
    
    check_username_emailID = "SELECT User_name,Email_ID FROM login_Data WHERE User_name = %s and Email_ID = %s;"
    checker_val = (generate_OTP_sys.username, generate_OTP_sys.emailid)
    mycursor.execute(check_username_emailID, checker_val)
    
        
    myresult = mycursor.fetchall()
    
    print(myresult)
    
    
    if myresult == []:
        generate_OTP['bg'] = "#ff3c69"
    else:
        print("success")
       
        generate_OTP['bg'] = "#06cca2"
        digits="0123456789"
        generate_OTP_sys.OTP=""

        for i in range(6):
            generate_OTP_sys.OTP+=digits[math.floor(random.random()*10)]
        otp = generate_OTP_sys.OTP + " is your OTP"
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()

        s.login("adityasharma0431@gmail.com", "jrthublquziceqdh")
        s.sendmail('&&&&&&&&&&&',generate_OTP_sys.emailid,msg)
    
    db_connect.commit()        


def OTP_Checker(OTp_sys,User_Name,Email,Check_OTP):
    OTPreceived = OTp_sys.get()
    # username = User_Name.get()
    # emailid = Email.get()
    
    
    # check_username_emailID = "SELECT * FROM login_Data WHERE User_name = %s and Email_ID = %s;"
    # checker_val = (username, emailid)
    # mycursor.execute(check_username_emailID, checker_val)
    
    
    # myresult = mycursor.fetchall()
    
    
    if(OTPreceived == generate_OTP_sys.OTP):
        Check_OTP['bg'] = "#06cca2"
        changeYour_psswd()
    else:
        Check_OTP['bg'] = "#ff3c69"
        


def Forget_psswd_OTP():

        # bg = PhotoImage(file = "pattern.png")
        # label1 = Label(forget_window, image = bg)   {{{{NOT WORKING!!!!!!!!!!!!}}}
        # label1.pack()
        


    def on_enter(e):
        Check_OTP['bg'] = '#fff'
        Check_OTP['fg'] = '#000'

    def on_leave(e):
        Check_OTP['bg'] = '#242424'
        Check_OTP['fg'] = '#9e9e9e'
        
    def on_enterr(e):
        cancelBttn['bg'] = '#fff'
        cancelBttn['fg'] = '#000'

    def on_leaver(e):
        cancelBttn['bg'] = '#242424'
        cancelBttn['fg'] = '#9e9e9e'
    
    def on_entero(e): 
        generate_OTP['bg'] = '#fff'
        generate_OTP['fg'] = '#000'

    def on_leaveo(e):
        generate_OTP['bg'] = '#242424'
        generate_OTP['fg'] = '#9e9e9e'
        
    



        
    frame = customtkinter.CTkFrame(root, width=430, height = 550, bg_color="#242424", corner_radius = 20 )
    frame.place(x = 530, y = 30)    

    heading = Label(frame,fg="#fff",bg="#2b2b2b",  text="Reset Password" ,font=('Century Gothic',28, 'bold'))
    heading.place(x=120,y=10)

    User_Name = customtkinter.CTkEntry(frame, width=350, height = 45 ,placeholder_text="Username", font=('Rod',15,'bold'))
    User_Name.place(x=30, y=80)
        
    Email = customtkinter.CTkEntry(frame, width=350, height = 45 , placeholder_text="Email Address", font=('Rod',15,'bold'))
    Email.place(x=30, y=150)
        
    OTp_sys = customtkinter.CTkEntry(frame, width=350, height = 45 , placeholder_text="OTP", font=('Rod',15,'bold'))
    OTp_sys.place(x=30, y=220)
        
    generate_OTP = Button(frame, text="generate OTP", border=0,  bg='#2b2b2b', fg="#9e9e9e", font=('Century Gothic',10), cursor='hand2', command= lambda: generate_OTP_sys(User_Name,Email,generate_OTP))
    generate_OTP.bind("<Enter>", on_entero)
    generate_OTP.bind("<Leave>", on_leaveo)
    generate_OTP.place(x=365 ,y = 335)

        # new_Password = customtkinter.CTkEntry(frame, width=350,height = 45 , placeholder_text="New Password", font=('Rod',15,'bold'))
        # new_Password.place(x=30, y=220)

        # confirm_Password = customtkinter.CTkEntry(frame, width=350,height = 45 , placeholder_text="Confirm New Password", font=('Rod',15,'bold'), show="*")
        # confirm_Password.place(x=30, y=290)
        
        # def show_psswd():
        #     confirm_Password.configure(show = "")
        #     hidePSSWD_button = Button(master=confirm_Password, image=hide_img ,bg="#343638", borderwidth=0, command=hide_psswd)
        #     hidePSSWD_button.place(x = 390, y = 14)
                
        # def hide_psswd():
        #     confirm_Password.configure(show = "*")
        #     showPSSWD_button = Button(master=confirm_Password, image=show_img ,bg="#343638", borderwidth=0, command=show_psswd)
        #     showPSSWD_button.place(x = 390, y = 14)

    

        # showPSSWD_button = Button(master=confirm_Password, image=show_img,  bg="#343638", borderwidth=0, command=show_psswd)
        # showPSSWD_button.place(x = 390, y = 14)

    cancelBttn = Button(master=frame, borderwidth = 0, width=15, height = 2 , fg="#9e9e9e", text="Cancel", bg='#242424', font=('Rod',15,'bold'), command=lambda: Sign_IN())
    cancelBttn.bind("<Enter>", on_enterr)
    cancelBttn.bind("<Leave>", on_leaver)
    cancelBttn.place(x = 280, y = 385)
        
        
    Check_OTP = Button(master=frame, borderwidth = 0, width=17, height = 2 , fg="#9e9e9e", text="Check", bg='#242424', font=('Rod',15,'bold'), command=lambda: OTP_Checker(OTp_sys,User_Name,Email,Check_OTP))
    Check_OTP.bind("<Enter>", on_enter)
    Check_OTP.bind("<Leave>", on_leave)
    Check_OTP.place(x = 43, y = 385)
    





def Forget_Auth(username,emailid,confirm_Password,Change_psswd,new_Password):
    
    confirm_psswd = confirm_Password.get()
    new_psswd = new_Password.get()
    
    if(new_psswd == confirm_psswd):
        
        check_userID_Phno = "SELECT * FROM login_Data WHERE User_name = %s and Email_ID = %s;"
        checker_val = (username,emailid)
        mycursor.execute(check_userID_Phno, checker_val)
        
        
        myresult = mycursor.fetchall()
        if myresult == []:
            pass
        else:    
            change = "UPDATE login_data SET Password = %s WHERE User_name = %s;"
            changing_val = (confirm_psswd, username)
            mycursor.execute(change, changing_val)
            Change_psswd['bg'] = "#06cca2"
            Sign_IN()
        
        db_connect.commit()
    else:
        Change_psswd['bg'] = "#ff3c69"
        print("Password didnt matched!!!")
        


def on_enter(e):
    Sign_inBttn['bg'] = '#fff'
    Sign_inBttn['fg'] = '#000'

def on_leave(e):
    Sign_inBttn['bg'] = '#242424'
    Sign_inBttn['fg'] = '#9e9e9e'

def Login_Auth():
    user_ID = User_Name.get()
    psswd = Password.get()
        
        
    check_userID_Passwd = "SELECT * FROM login_Data WHERE User_name = %s and Password = %s;"
    checker_val = (user_ID, psswd)
    mycursor.execute(check_userID_Passwd, checker_val)
        
        
    myresult = mycursor.fetchall()
        
    if myresult  == []:
        Sign_inBttn['bg'] = "#ff3c69"
    else:
        Sign_inBttn['bg'] = "#06cca2"
        mian.logo() 
        
    


def Sign_IN():
    def on_enter(e):
        Sign_inBttn['bg'] = '#fff'
        Sign_inBttn['fg'] = '#000'

    def on_leave(e):
        Sign_inBttn['bg'] = '#242424'
        Sign_inBttn['fg'] = '#9e9e9e'

    def Login_Auth():
        user_ID = User_Name.get()
        psswd = Password.get()
        
        
        check_userID_Passwd = "SELECT * FROM login_Data WHERE User_name = %s and Password = %s;"
        checker_val = (user_ID, psswd)
        mycursor.execute(check_userID_Passwd, checker_val)
        
        
        myresult = mycursor.fetchall()
        
        if myresult  == []:
            Sign_inBttn['bg'] = "#ff3c69"
        
        else:
            Sign_inBttn['bg'] = "#06cca2"
            mian.logo()
            
   
            
    
    frame = customtkinter.CTkFrame(root, width=430, height = 550, bg_color="#242424", corner_radius = 20 )
    frame.place(x = 530, y = 30)

    heading = Label(frame,fg="#fff",bg="#2b2b2b",  text="Log into your Account",font=('Century Gothic',28, 'bold'))
    heading.place(x=73,y=5)

    User_Name = customtkinter.CTkEntry(frame, width=350, height = 45, placeholder_text="Username", font=('Rod',15,'bold'))
    User_Name.place(x=38, y=80)
    
    def show_psswd():
        Password.configure(show = "")
        hidePSSWD_button = Button(master=Password, image=hide_img ,bg="#343638", borderwidth=0, command=hide_psswd)
        hidePSSWD_button.place(x = 390, y = 14)
            
    def hide_psswd():
            Password.configure(show = "*")
            showPSSWD_button = Button(master=Password, image=show_img ,bg="#343638", borderwidth=0, command=show_psswd)
            showPSSWD_button.place(x = 390, y = 14)




    Password = customtkinter.CTkEntry(frame, width=350,height = 45 , placeholder_text="Password", font=('Rod',15,'bold'), show="*")
    Password.place(x=38, y=150)
    
    showPSSWD_button = Button(master=Password, image=show_img,  bg="#343638", borderwidth=0, command=show_psswd)
    showPSSWD_button.place(x = 390, y = 14)
    

    Sign_inBttn = Button(frame, borderwidth = 0, width=35 ,height = 2 , fg="#9e9e9e", text="Sign in", bg='#242424', font=('Rod',15,'bold'), command=lambda: Login_Auth())
    Sign_inBttn.bind("<Enter>", on_enter)
    Sign_inBttn.bind("<Leave>", on_leave)
    Sign_inBttn.place(x = 48, y = 280)
    
    forget_pss = Button(frame, text="forget password?", border=0,  bg='#2b2b2b', fg="#9e9e9e", font=('Century Gothic',10), cursor='hand2', command = Forget_psswd_OTP)
    forget_pss.place(x=350 ,y = 246)


    label3 = Label(frame, text="Don't have an Account?", fg="#9e9e9e", bg="#2b2b2b", font=('Century Gothic',10))
    label3.place(x=238, y = 353)

    signUP = Button(frame, text="Sign Up", border=0,  bg='#242424', fg="white", font=('Century Gothic',10), cursor='hand2', command=lambda :Sign_UP())
    signUP.place(x=405, y = 351)



def Sign_UP():
    
    def on_enter(e):
        Sign_upBttn['bg'] = '#fff'
        Sign_upBttn['fg'] = '#000'

    def on_leave(e):
        Sign_upBttn['bg'] = '#242424'
        Sign_upBttn['fg'] = '#9e9e9e'
    
    frame = customtkinter.CTkFrame(root, width=430, height = 550, bg_color="#242424", corner_radius = 20 )
    frame.place(x = 530, y = 30)

    heading = Label(frame,fg="#fff",bg="#2b2b2b",  text="Registration",font=('Century Gothic',28, 'bold'))
    heading.place(x=162,y=5)

    Full_Name = customtkinter.CTkEntry(frame, width=350, height = 45, placeholder_text="Full Name", font=('Rod',15,'bold'))
    Full_Name.place(x=38, y=80)
    
    User_Name = customtkinter.CTkEntry(frame, width=350, height = 45, placeholder_text="Username", font=('Rod',15,'bold'))
    User_Name.place(x=38, y=150)
    
    Email_id = customtkinter.CTkEntry(frame, width=350, height = 45, placeholder_text="Email Address", font=('Rod',15,'bold'))
    Email_id.place(x=38, y=221)

    Password = customtkinter.CTkEntry(frame, width=350,height = 45 , placeholder_text="Password", font=('Rod',15,'bold'), show="*")
    Password.place(x=38, y=291)
    
    label3 = Label(frame, text="Already have an Account?", fg="#9e9e9e", bg="#2b2b2b", font=('Century Gothic',10))
    label3.place(x=225, y = 525)

    signin = Button(frame, text="Sign In", border=0,  bg='#242424', fg="white", font=('Century Gothic',10), cursor='hand2', command=lambda :Sign_IN())
    signin.place(x=405, y = 523)
    
    Sign_upBttn = Button(master=frame, borderwidth = 0, width=35 ,height = 2 , fg="#9e9e9e", text="Sign up", bg='#242424', font=('Rod',15,'bold'), command=lambda: Register(Full_Name,User_Name,Email_id,Password))
    Sign_upBttn.bind("<Enter>", on_enter)
    Sign_upBttn.bind("<Leave>", on_leave)
    Sign_upBttn.place(x = 48, y = 456)



###############################################################



btt = PhotoImage(file = "back.png")
label1 = Label( root, image = btt)
label1.pack()


img = PhotoImage(file = "logo2.png")
label2 = Label(root, image = img, bg="#242424", width=380, height=186)
label2.place(x = 120, y = 260)

frame = customtkinter.CTkFrame(root, width=430, height = 550, bg_color="#242424", corner_radius = 20 )
frame.place(x = 530, y = 30)

heading = Label(frame,fg="#fff",bg="#2b2b2b",  text="Log into your Account",font=('Century Gothic',28, 'bold'))
heading.place(x=73,y=5)

User_Name = customtkinter.CTkEntry(frame, width=350, height = 45, placeholder_text="Username", font=('Rod',15,'bold'))
User_Name.place(x=38, y=80)

def show_psswd():
        Password.configure(show = "")
        hidePSSWD_button = Button(master=Password, image=hide_img ,bg="#343638", borderwidth=0, command=hide_psswd)
        hidePSSWD_button.place(x = 390, y = 14)
            
def hide_psswd():
        Password.configure(show = "*")
        showPSSWD_button = Button(master=Password, image=show_img ,bg="#343638", borderwidth=0, command=show_psswd)
        showPSSWD_button.place(x = 390, y = 14)



Password = customtkinter.CTkEntry(frame, width=350,height = 45 , placeholder_text="Password", font=('Rod',15,'bold'), show="*")
Password.place(x=38, y=150)

showPSSWD_button = Button(master=Password, image=show_img,  bg="#343638", borderwidth=0, command=show_psswd)
showPSSWD_button.place(x = 390, y = 14)


Sign_inBttn = Button(master=frame, borderwidth = 0, width=35 ,height = 2 , fg="#9e9e9e", text="Sign in", bg='#242424', font=('Rod',15,'bold'), command=lambda: Login_Auth())
Sign_inBttn.bind("<Enter>", on_enter)
Sign_inBttn.bind("<Leave>", on_leave)
Sign_inBttn.place(x = 48, y = 280)

forget_pss = Button(frame, text="forget password?", border=0,  bg='#2b2b2b', fg="#9e9e9e", font=('Century Gothic',10), cursor='hand2', command=Forget_psswd_OTP)
forget_pss.place(x=350 ,y = 246)

label3 = Label(frame, text="Don't have an Account?", fg="#9e9e9e", bg="#2b2b2b", font=('Century Gothic',10))
label3.place(x=238, y = 353)

signUP = Button(frame, text="Sign Up", border=0,  bg='#242424', fg="white", font=('Century Gothic',10), cursor='hand2', command=lambda :Sign_UP())
signUP.place(x=405, y = 351)

 
root.mainloop()

import mysql.connector
import stdiomask


def Registration():
    Full_name = input("Enter Your Full Name:-  ")
    User_name = input("Enter You User Name:-   ")
    Phone_no = input("Enter your Phone Number(10 digits):- ")
    Password = input("Enter your Password:-    ")

    insertion = "INSERT INTO login_Data values(%s,%s,%s,%s)"
    val_insertion = (Full_name, User_name, Phone_no, Password)

    mycursor.execute(insertion, val_insertion)

    

def Login():
    
    UserID_input = input("Enter your User Name:- ")
    Password_input = stdiomask.getpass("Enter your Password:- ")
    
    
    check_userID_Passwd = "SELECT * FROM login_Data WHERE User_name = %s and Password = %s;"
    checker_val = (UserID_input, Password_input)
    mycursor.execute(check_userID_Passwd, checker_val)
    
    
    myresult = mycursor.fetchall()
    
    if myresult  == []:
        print("Wrong Initials!!!!!!")
        return False
    
    else:
        while(True):
            print("HELLO THERE")
            break
        
            

def forget_Passwd():
    user = input("Enter your User ID: ")
    phno = input("Enter registered Phone number: ")
    
    check_userID_Phno = "SELECT * FROM login_Data WHERE User_name = %s and Phone_no = %s;"
    checker_val = (user, phno)
    mycursor.execute(check_userID_Phno, checker_val)
    
    
    myresult = mycursor.fetchall()
    if myresult == []:
        print("Wrong Initials!!!!")
        return False
    else:    
        new_password = input("Enter your new Password: ")
        
        change = "UPDATE login_Data SET Password = %s WHERE User_name = %s;"
        changing_val = (new_password, user)
        
        mycursor.execute(change, changing_val)


###########################################################
###########################################################
###########################################################


switch_ONN = True

while(switch_ONN):
    db_connect = mysql.connector.connect(
            host='localhost',
            user ='root',
            port='3307',
            password='',
            database='techienaman');

    mycursor = db_connect.cursor();
    
    print("{Welcome to Trading Monk}")
    print("Do u want Register or Login:")
    print("==>>1.Register")
    print("==>>2.Login")
    print("==>>3.Forget Password")
    
    register_Login = input("")
    
    if(register_Login == "1"):
        Registration();
    
    elif(register_Login == "2"):
        login = Login();
        if login == False:
            switch_ONN = False
            
    elif(register_Login == "3"):
        forget_passwd = forget_Passwd();
        if forget_passwd == False:
            switch_ONN = False      
             
    db_connect.commit()
#HI,welcomes you in spy_chat
import chat #calling chat file
while 1==1:
    print"###WELCOME BACK TO SPYCHAT###"#greetings
    print"SELECT OPTION"
    print"\t1.LOG IN:\n\t2.SIGN UP:"
    choose = raw_input("")
    if choose == "2" or choose == "2":
        i = False
        while i != True:#loop added
            #taking a,spy as a variable
            a=raw_input("Mr/Mrs?:")#salutation
            b=raw_input("Enter your name:")#spy_name
            c=raw_input("Enter your age:")#spy_age
            d=raw_input("Enter your rating:")#spy_rating
            spy=chat.Name(a,b,c,d)#calling class from chat into varible'''
         #creating a username and password
            print"USER-NAME:"
            createun=raw_input()
            print"PASS-WORD:"
            createps=raw_input()
            print "Thanks for signing up"
            break;                #breaking loop here

    else:
        while 1==1:               #added loop
            print"USER-NAME:"     #creating user name for sign up user
            createun = raw_input()
            print"PASS-WORD:"     #creating password for sign up user
            createps = raw_input()
            print "Thanks for signing up:" #greetings
            break;                #breaking loop here
        while 1==1:
            print "Enter your username:"#created username
            loginun = raw_input()
            if createun == loginun:
                print "Enter your password:"#created password
                loginps = raw_input()
                if createps == loginps:
                   print "login sucessful:!!!"
                   break;
                else:
                   print"Password incorrect"
                   break;
            else:
                print "login failed!!!\t re-enter"




    chat.msg_check() # moving to chat file

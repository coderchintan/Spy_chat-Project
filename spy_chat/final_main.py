#/home/chintan/Downloads/spy_chat.zip
from final import spy,choose_member,add_status,add_friend,send_message,read_message,read_chat
# Choose user
print"welcome to the spy_chat"
while True:
    password=raw_input("enter your password")
    if password=="chintan":
        print "verified"
        break
    else:
        print " not verified \n pleae re-enter"

while True:
    choice = raw_input("Do you  want to continue as the default user(Y/N) :")
    if choice == 'Y' or choice == 'y':
        active = choose_member(choice)
        break
    elif choice == 'N' or choice == 'n':
        active = choose_member(choice)
        break
    else:
        print "Invalid input.Please re-enter "

print "\n\t\tWelcome  to menu %s %s\n" % (active.sal,active.name)
print "Select what you want to do\nraw- been:"
i=True
current_stat = None
while i:
    # Main menu of spy_chat
    scan = raw_input("\t\t1) Add a status update\n\t\t2) Add a friend\n\t\t3) Send a secret message\n"\
    "\t\t4) Read a secret message\n\t\t5) Read chats from a user\n\t\t6) Close application ")
    if scan == '1':
        print "Current account status :%s" % current_stat
        current_stat = add_status(active)
        print "Updated status: %s" % current_stat
    elif scan == '2':
        tot = add_friend(active)
        print "Total friend :%d" % tot
        for temp in active.friends:
            print "* %s" % temp.name
    elif scan == '3':
        s = send_message(active)
        if s != 0:
            print "Message saved"
    elif scan == '4':
        m = read_message(active)
        if m == 'SOS':
            print "You got an emergency message\n\tSOS!!!!SOS!!!SOS!!!!\n"
        elif m == 'SAVE ME':
            print "Code red message\n\tSAVE ME!!!!SAVE ME!!!!\n"
        elif m == 'OP':
            print "Call for operation\n\tTIME TO GOOOOO!!!!\n"
        elif m == 0:
            continue
        else:
            print "Message :%s" % m
    elif scan == '5':
        read_chat(active)
    elif scan == '6':
        print "Have a good day"
        i=False
    else:
        print "Invalid input.Re-enter"









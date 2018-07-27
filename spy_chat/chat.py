from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored,cprint
class Name:
    def __init__(self, salutation, spy_name, age, rating):
        self.salutation = salutation
        self.spy_name = spy_name
        self.age = age
        self.rating = rating
        self.chat = []
list_friend=[]
old_status = ["blind", "love", "sick"]
text =[]
current_status = None
lol = None
def msg_check():
                                                       # starting hike chating
    print"Starting hike chating"
    while 1 == 1:                                      #added loop here
                                                       # \t refers tab and \n refers to new line
                                                       #chating menu opening
        print"\t1.friend list\n\t2.Status update\n\t3.Inbox\n\t4.Back"
        choice = int(raw_input())                      # choice for entering into friend list
        if choice == 1:                                #entering choice in int
            print"Opening firend list"

            while 1 == 1:                              #loop added
                print"\t1.Add-friend\n\t2.select friend\n\t3.back"
                option = int(raw_input())
                if option == 1:
                    salutation=raw_input("Mr/Mrs:")                           #salution
                    spy_name=raw_input("Enter your name:")                    #spy_name
                    age=int(raw_input("Enter your age:"))                     #spy_age
                    rating=float(raw_input("Enter your ratings:"))            #spy_rating
                                                      #calling class into variable
                    frn = Name(salutation,spy_name,age,rating)
                    print "adding..."
                    print "your added to my friend list", '-' + frn.spy_name
                                                #inserting frn variable into list of list_friend
                    list_friend.append(frn)

                                                #selecting friend from friend_list
                                                #checkout friends position
                elif option == 2:
                    print "select a friend"
                    item_number = 1
                    for new_friend in list_friend:
                        print "%d.%s" % (item_number,new_friend.spy_name)
                        item_number = item_number + 1
                    friend_choice = raw_input("choose from your friends")

                    friend_choice_position=int(friend_choice)-1
                    print "selected friend %s" \
                          % list_friend[friend_choice_position].spy_name
                elif option == 3:
                    print "starting hike chating"
                    print choice                #calling  hike message menu
                    break;                      #closing loop here
        elif choice == 2:
            while 1==1:                         #loop added
                print"Opening status update"    #opening status menu
                print"\t1.update\n\t2.Old-status\n\t3.back"
                choose = int(raw_input())
                if choose == 1:
                    print"loading..."
                    new_message = raw_input("Enter new status:-")
                    old_status.append(new_message)      #inserting newmessage in old_status list
                    print"updating....", (new_message)
                    current_status = new_message        #current status
                    print "your current status:-" + current_status
                if choose == 2:
                    print old_status
                    print"select an old-status"
                    item = 1
                    for temp in old_status:
                        print "%d. %s" % (item, temp)
                        item = item + 1
                    spam = int(raw_input("Enter your choice:"))
                    new_message = old_status[spam - 1]
                    old_status.append(new_message)
                    print "Old-status updating... " + new_message
                    current_status = current_status
                    print "your current status:" + current_status
                    break;

                if choose ==3:                         #calling hike message menu here
                    print "start hike chating"
                    print choice

        elif choice == 3:
            while 1==1:                                #loop added
                print "opening chat message"           #opening chat_message menu
                print "\t1. Sending message\n\t2. Read message\n\t3.Chat history\n\t4.back"
                select= int(raw_input())
                if select== 1:
                    item_number = 1
                    for new_friend in list_friend:
                        print "%d.%s" % (item_number, new_friend.spy_name) #string and int added
                        item_number = item_number + 1
                    friend_choice = raw_input("choose from your friends")

                    friend_choice_position = int(friend_choice)
                    friend_choice_position = friend_choice_position -1
                    print "selected friend %s" \
                          % list_friend[friend_choice_position].spy_name
                    original_image = raw_input("What is the name of the image?")#path of image
                    output_path = raw_input('output.jpg:')                #out-put path of image
                    text = raw_input("What do you want to say?")          #number of words
#hiding secret messsage in pictures (encode by steganograpy

                    Steganography.encode(original_image, output_path, text)
                    new_chat = {                                  #adding dictionary here
                        "message": text,
                        "time": datetime.now(),
                        "delivered": True,'by_me':True
                    }
                                                             #adding dictionary into friend_list
                    list_friend[friend_choice_position].chat.append(new_chat)

                elif select== 2:

                    item_number = 1
                    for new_friend in list_friend:
                        print "%d.%s" % (item_number, new_friend.spy_name)
                        item_number = item_number + 1
                    friend_choice = raw_input("choose from your friends")

                    friend_choice_position = int(friend_choice)
                    friend_choice_position = friend_choice_position -1
                    output_path= raw_input("path of the output.jpg:")
                    text = Steganography.decode(output_path)
                    print "Decoded message :%s" % text
                    if text=="SOS":                               #emergency code message
                        print "save our souls"
                    elif text=="save me":
                        print "Emergency needs"
                        new_chat = {
                            "message": text,
                            "time": datetime.now(),
                            "delivered": True,'by_me':False
                        }

                    list_friend[friend_choice_position].chat.append(new_chat)
                elif select==3:
#importing datetime and termcolor

                    print ("opening chat history")
                    item_number = 1
                    for new_friend in list_friend:
                        print "%d.%s" % (item_number, new_friend.spy_name)
                        item_number = item_number + 1
                    friend_choice = int(raw_input("choose from your friends"))
                    friend_choice = friend_choice - 2
                    for temp in list_friend[friend_choice].chat:
                        cprint("[%s] "% temp['time'],"blue",attrs=['bold'])
                        cprint("message:%s" % temp["message"])
                        cprint("new_friend:%s" % new_friend.spy_name, "red")
                        print colored("%s" % datetime.now(),"blue")
                        if temp['by_me']==True:
                            print "Sent by me"
                        elif temp['by me']==False:
                            print "Sent by other"
                            text=text.split()                   #split is use to calculate word

#calculating text more than 100 words delete spy_friend chat

                        elif len(text)>100:
                            print "maximum message found!!!\t DELETE MESSAGE"
                            del list_friend[1]                  #deleting friend chat here


                elif select==4:
                    print"start hike chating"
                    print choice                                #returning to hike message menu
                    break;
        elif choice == 4:
            print choice
            break;
#loop continue to login and sign up
#end of coding here
































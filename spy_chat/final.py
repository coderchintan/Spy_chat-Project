# Spy_class
class spy:
    def __init__(self,spy_name,spy_sal,spy_age,spy_rating):
        self.name = spy_name               # Spy name
        self.sal = spy_sal                 # Spy salutation
        self.age = int(spy_age)            # Spy age
        self.rating = float(spy_rating)    # Spy rating
        self.status_message = []           # Spy status message list
        self.friends = []                  # Spy friend list
        self.by_me = None                  # Message sender indicator
        self.chat = []                     # Chat list of a friend

# Chat_class(For timestamps)
class chats:
    def __init__(self,mess,time,stat,words):
        self.message = mess
        self.time = time
        self.by_me = stat
        self.av_words = words

# Choosing or creating new user
def choose_member(choice):

    if choice == 'Y' or choice == 'y':
        default = spy('rabin', 'Mr', 21, 5)
        default.is_online = True
        return default                     # Default user
    mem = create()
    return mem                             # New user


# Add or update the status
def add_status(active):
    while True:
        temp = raw_input("1.Older status\n2.Create new :")
        if temp == '1':
            item = 1
            for temp in active.status_message:
                print "\t\t%d. %s" % (item, temp)
                item = item + 1
            while True:
                i = raw_input("\nSelect :")
                try:
                    i=int(i)
                except ValueError:
                    print "Invalid input.Re-enter(in numbers only)"
                    continue
                break
            # Error handling for empty status lists
            try:
                updated_stat = active.status_message[i - 1]
            except IndexError:
                print "Status list empty.Please enter status first"
                return 0
            return updated_stat
        elif temp == '2':
            updated_stat = raw_input("\nEnter status: ")
            active.status_message.append(updated_stat)
            return updated_stat
        else:
            print "\nInvalid Input.Please re-enter\n"



# Create a user or friend
def create():
    i = True
    while i:
        new_name = raw_input('\n\t\tEnter name :')
        if len(new_name) == 0:
            print "\t\tInvalid input"
        else:
            i = False
    new_sal = raw_input("\t\tMr/Mrs ?")
    while True:
        try:
            new_age = int(raw_input("\t\tEnter age :"))
        except ValueError:
            print "\t\tInvalid input.Please re-enter(in numbers only)"
            continue
        if (new_age < 12 or new_age > 50):
            print "\t\tInconvenient age. Please enter a age b/w (12-50) "
            continue
        else:
            break
    buff = True
    while buff:
        try:
            new_rating = float(raw_input("\t\tEnter rating :"))
        except ValueError:
            print "\t\tInvalid rating. Please enter(in numbers only)"
            continue
        if new_rating > 7 and new_rating <= 10:
            print "\t\tSir, you are one of the elites"
            buff = False
        elif new_rating > 4 and new_rating <= 7:
            print "\t\tYou are one hell of an agent"
            buff = False
        elif new_rating > 0 and new_rating <= 4:
            print "\t\tWork hard agent,success is yours"
            buff = False
        else:
            print "\t\tInvalid rating.Please re-enter"

    new_user = spy(new_name, new_sal, new_age, new_rating)    # Creating spy class instance
    new_user.is_online = True
    return new_user                                           # New user

# Add a friend in the friend list of the current user
def add_friend(active):

    friend = create()                     # Creating friend of active spy
    active.friends.append(friend)         # Appending friend to friend list
    return len(active.friends)            # Length of friend list

# Select a friend from the friend list
def sel_friend(active):
    item = 1
    for temp in active.friends:
        print "%d. %s" % (item,temp.name)
        item = item + 1
    while True:
        try:
            sel = int(raw_input("Select :"))
        except ValueError:
            print "Invalid input.Please re-enter(numbers only)"
            continue
        break
    return sel-1

# Send a message to the friends of the current user
def send_message(active):
    from datetime import datetime
    from steganography.steganography import Steganography
    sel = sel_friend(active)
    image_name = raw_input("Enter name of image :")         # Path of the image file (unmodded)
    message = raw_input("Enter message :")
    out_name = image_name
    print "\n...Loading...\n"
    # Error handling for wrong file path or name
    try:
        Steganography.encode(image_name,out_name,message)
    except:
        print "Error while encoding\nHint: See file name"
        return 0
    # Error handling for empty friend list
    try:
        new_chat = chats(message,datetime.now(),True,av_words(active.friends[sel]))
        active.friends[sel].chat.append(new_chat)
    except IndexError:
        print "Friend list empty.Please add a friend first"
        return  0

# Read a message from the friends of the current user
def read_message(active):
    from datetime import datetime
    from steganography.steganography import Steganography
    sel = sel_friend(active)                                     # Selecting friend
    image_name = raw_input("Enter the name of encrypted image")  # Name of the modded image(default path)
    print "\t\t\n...Loading....\n"

    # Handling error for unencrypted(unmodded) image
    try:
        #
        message = Steganography.decode(image_name)
    except:
        print "Error(TypeError).Please enter encrypted image"
        return 0
    # Error handling for empty friend list
    try:
        words = av_words(active.friends[sel])
        new_chat = chats(message, datetime.now(), False, words)
        active.friends[sel].chat.append(new_chat)
    except IndexError:
        print "Friend list empty.Add a friend first"
        return 0

    # Deleting friend who speaks more than 100 words
    if words >=100:
        print "%s have been deleted from ur friend list(speaks too much)" % active.friends[sel]
        del active.friends[sel]
    return message

# Read entire chat of a friend
def read_chat(active):
    from termcolor import colored,cprint
    import termcolor
    sel = sel_friend(active)
    # Error handling for empty friend list
    try:

        for temp in active.friends[sel].chat:
            time = '[Time :%s]' % temp.time
            mess = '[Message :%s]' % temp.message
            by = '[By_me :%s]' % temp.by_me
            print colored(time, 'green'),
            print colored(mess, attrs=['bold']),
            print colored(by, 'blue')
    except IndexError:
        print "Friend list empty.Add a friend first"

# Average words spoken by a spy friend
def av_words(friend):
    av = 0
    for temp in friend.chat:
        av = av + int(len(temp.message)/4)
    return av                                # Return total average words spoken by a friend



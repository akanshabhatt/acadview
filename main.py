from spydetails import spy
Status_messages=['Keep Calm','Peace','Do not disturb']
friends=[]
print "Welcome to SpyChat!"
choice =raw_input("Do you want to continue as " + spy['spy_salutation'] + " " + spy['spy_name'] + " (Y/N)? ")

def add_friend():
    new_friend = {
        'new_name': '',
        'new_salutation': '',
        'new_age': 0,
        'new_rating': 0.0
    }
    new_friend['new_name']=raw_input("What is your friend's name?")
    if len(new_friend['new_name'])>0:
        new_friend['new_salutation']=raw_input("Are you Mr. or Ms.?")
        new_friend['new_name']=new_friend['new_salutation']+" "+new_friend['new_name']
        new_friend['new_age'] = int(raw_input("What is your friend's age?"))
        if (new_friend['new_age'])>12 and (new_friend['new_age'])<=50:
            new_friend['new_rating'] = float(raw_input("What is your friend's rating?"))
            friends.append(new_friend)
            print "Friend is added"
        else:
            print "Age entered is invalid."
    else:
        print "Name entered is invalid."
    return len(friends)

def add_status(current_status_message):
    updated_status_message=None
    if current_status_message!=None:
        print "Your current status is:  %s" %(current_status_message)
    else:
        print "You don't have any current status"
    ques=raw_input("Do you want to choose from the older status message? (Y/N)")
    if ques=='Y' or ques=='y':
        message_position=1;
        for message in Status_messages:
            print "%d. %s" %(message_position,message)
            message_position+=1
        message_choice=int(raw_input("Choose from the above messages."))
        if len(Status_messages)>=message_choice:
            updated_status_message=Status_messages[message_choice-1]
        else:
            print "Invalid message choice."
    elif ques=='N' or ques=='n':
        new_status=raw_input("Write your new status update.")
        if len(new_status)>0:
            Status_messages.append(new_status)
            updated_status_message=new_status
    else:
        print "Invalid choice."
    if updated_status_message:
        print "Your updated status is %s" %(updated_status_message)
    else:
        print "You have not updated your status."
    return updated_status_message


def chat(spy):
    current_status_message = None
    if (spy['spy_age'])>12 and (spy['spy_age'])<50:
        spy['spy_name'] = spy['spy_salutation'] + " " + spy['spy_name']
        if spy['spy_rating'] > 4:
            print 'Great going!'
        elif spy['spy_rating'] > 3 and spy['spy_rating'] <= 4:
            print 'You are one of the good ones.'
        elif spy['spy_rating'] >= 2.5 and spy['spy_rating'] <= 3:
            print 'You can always do better'
        else:
            print 'You need to work harder.'
        spy['spy_online_status']=True
        print "Authentication complete. Welcome " + spy['spy_name'] + " age: " + str(spy['spy_age']) + " and rating of: " + str(spy['spy_rating']) + " Proud to have you onboard."
        menu=True
        while menu:
            print "1.Add a status update"
            print "2.Add a friend"
            print "3.Send a secret message"
            print "4.Read a secret message"
            print "5.Read chats from a user"
            print "6.Close application"
            ch=int(raw_input("What is your choice?"))
            if ch==1:
                current_status_message=add_status(current_status_message)
            elif ch==2:
                no_of_friends=add_friend()
                print "The spy has %d friends" %(no_of_friends)
            else:
                menu=False

    else:
        print "You are not of the correct age to be a spy."


if choice=='Y' or choice=='y':
    chat(spy)
elif choice=='N' or choice=='n':
    spy={
        'spy_name' : '',
        'spy_salutation' : '',
        'spy_age' : 0,
        'spy_rating' : 0.0,
        'spy_online_status' : False
    }
    spy['spy_name'] = raw_input("Welcome to SpyChat, please tell your spyname first :")
    spy['spy_online_status'] = False
    if len(spy['spy_name']) > 0:
        print "Welcome " + spy['spy_name'] + " Glad to have you back."
        spy['spy_salutation'] = raw_input("Should I call you Mr. or Ms.?")
        spy['spy_online_status']=True
        print "Alright " + spy['spy_name'] + " I'd like to know a little bit more about you before we proceed..."
        spy['spy_age'] = int(raw_input("What is yor age?"))
        spy['spy_rating'] = float(raw_input("What is your spy rating?"))
        chat(spy)
    else:
        print "The Spyname entered was invalid.Try again."
else:
    print "Enter a valid choice"



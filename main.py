from spydetails import spy_name, spy_salutation, spy_rating, spy_age, spy_online_status
Status_messages=['Keep Calm','Peace','Do not disturb']
print "Welcome to SpyChat!"
choice =raw_input("Do you want to continue as " + spy_salutation + " " + spy_name + " (Y/N)? ")
def add_status(current_status_message):
    updated_status_message=None
    if current_status_message!=None:
        print "Your current status is %s" %(current_status_message)
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
            Status_message=Status_messages.append(new_status)
            updated_status_message=new_status
    else:
        print "Invalid choice."
    if updated_status_message:
        print "Your updated status is %s" %(updated_status_message)
    else:
        print "You have not updated your status."
    return updated_status_message


def chat(spy_name,spy_age,spy_rating,spy_online_status):
    current_status_message = None
    if spy_age>12 and spy_age<50:
        spy_name = spy_salutation + " " + spy_name
        if spy_rating > 4:
            print 'Great going!'
        elif spy_rating > 3 and spy_rating <= 4:
            print 'You are one of the good ones.'
        elif spy_rating >= 2.5 and spy_rating <= 3:
            print 'You can always do better'
        else:
            print 'You need to work harder.'
        spy_online_status=True
        print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard."
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
            else:
                menu=False

    else:
        print "You are not of the correct age to be a spy."


if choice=='Y' or choice=='y':
    chat(spy_name,spy_age,spy_rating,spy_online_status)
elif choice=='N' or choice=='n':
    spy_name = raw_input("Welcome to SpyChat, please tell your spyname first :")
    spy_online_status = False
    if len(spy_name) > 0:
        print "Welcome " + spy_name + " Glad to have you back."
        spy_salutation = raw_input("Should I call you Mr. or Ms.?")
        spy_online_status=True
        print "Alright " + spy_name + " I'd like to know a little bit more about you before we proceed..."
        spy_age = int(raw_input("What is yor age?"))
        spy_rating = float(raw_input("What is your spy rating?"))
        chat(spy_name,spy_age,spy_rating,spy_online_status)
    else:
        print "The Spyname entered was invalid.Try again."
else:
    print "Enter a valid choice"



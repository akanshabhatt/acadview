spy_name=raw_input("Welcome to SpyChat, please tell your spyname first :")
if len(spy_name)>0:
    print "Welcome "+spy_name+" Glad to have you back."
    spy_salutation=raw_input("Should I call you Mr. or Ms.?")
    spy_name=spy_salutation+" "+spy_name
    print "Alright "+spy_name+" I'd like to know a little bit more about you before we proceed..."
    spy_age=int(raw_input("What is yor age?"))
    if spy_age>12 and spy_age<50:
        spy_rating=float(raw_input("What is your spy rating?"))
        if spy_rating > 4:
            print 'Great going!'
        elif spy_rating > 3 and spy_rating <= 4:
            print 'You are one of the good ones.'
        elif spy_rating >= 2.5 and spy_rating <= 3:
            print 'You can always do better'
        else:
            print 'You need to work harder.'
        print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard."
    else:
        print "You are not of the correct age to be a spy."
else:
    print "The Spyname entered was invalid.Try again."
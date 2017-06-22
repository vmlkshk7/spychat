print "Hello User.. Welcome to SPYCHAT..!! :D"
from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


spy=Spy

friends = []


#ask spy name
Spy.name = raw_input("What is your Spy name: ")
if len(spy.name)>0:
    print "Welcome " + Spy.name + "... We are happy to have you on Spychat...:)"

    #spy salutation
    Spy.salutation = raw_input("Should I call you Mr. or Ms. ? ")
    Spy.name = Spy.salutation + " " + Spy.name
    print "Alright " + Spy.name + " I'd like to know a little more about you before we proceed.. Please us know more about you with giving us few of your details.."

    Spy.age=0
    Spy.rating=0.0
    Spy.is_online=False
    Spy.age = raw_input("What is your Age?  ")

    #raw input always give a strig. so we need to convert this into integer.
    Spy.age= int(Spy.age)

    #Age cannot be less than 12 and no spies greater than 50 are allowed to exist
    #For condition check we are using Nested If

    if Spy.age>12 and Spy.age<50:

        Spy.rating = raw_input("What is your Spy Rating?  ")
        Spy.rating = float(Spy.rating)

        if Spy.rating > 4.5:
            print "Great Ace.."
        elif Spy.rating > 3.5 and Spy.rating <=4.5 :
            print "You are one of the good ones"
        elif Spy.rating >= 2.5 and Spy.rating<=3.5 :
            print "You can always do better"
        else:
            print"We can always use somebody to help in the office"

        #online
        Spy.is_online= True



        #one final message with all the details
        print "Authentication complete.. Welcome "+ Spy.name +" age: "+ str(Spy.age) + " and rating of: " + str(Spy.rating) + "... Proud to have you on Board"


    else:
        print "Sorry you are not of the correct age to be a spy... :("

else:
    print "A spy needs to have a valid name. Try again please"
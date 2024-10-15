
choicestairs=""
choiceleft=""
choiceright=""
choiceevade=""
choiceone=""
choiceone=input("You wake up feeling very groggy, with a splitting headache and blurry vision. As it clears, you find yourself within a dimly lit mansion. Its the middle of the night, and you hear sounds of a storm outside. The mansion is eerily silent, with only a dozen candles to light your view. You seem to be in the entry room of the mansion, with a staircase leading to a second floor, a door to the right and left, and a set of double doors on the far wall. Do you go up the STAIRS, to the LEFT, or to the RIGHT?")
#First Choice Responses
if choiceone.lower()=="left":
    choiceleft=input("You choose the left door, and find yourself in the dining room, a large rectangular table stretches out before you, filled with surprisingly warm and fresh food of all kinds. Turkey, sausage, beef, potatoes, carrots, and rolls. Near the end of the table, there was also a small array of desserts, some cookies and cakes and such. You gratefully dig in, as you realize how hungry you are. In the middle of eating, you hear a loud bang come from under the table. Do you either, LOOK under the table, GRAB some food for the road and go, or simply continue EATING?")
elif choiceone.lower()=="stairs":
    choicestairs=input("You stand up, gathering yourself, and begin to move your way up the stairs, as you do, the boards creak beneath your feet. About midway up, a cold wind blows through a broken window, which chills you to the bone. As you look up to the window, you see something else blew in as well. A large bat, flies in, shrieking and screaming. Do you try to FIGHT the bat, do you RUN away, or do you EVADE the bat, and keep climbing the stairs?")
elif choiceone.lower()=="right":
    choiceright=input("You choose the right door")
elif choiceone.lower() in("leave","double doors","doors"):
    secondchoice=input("Alabaster")
else: print("") 

if choiceone.lower() not in("left","stairs","right","leave","double doors","doors") : print("I'm sorry, but that wasn't one of the designed options, please type in one of the words that are in all caps, or maybe you might get lucky in picking something not in caps, who knows? But seriously, just pick one of the all caps words, you need to get lucky to find the secrets.") 

#Second Choice Responses

if choicestairs.lower()=="run":
    choicerun=input("Hassen")
elif choicestairs.lower()=="fight":
    choicefight=input("Pie")
elif choicestairs.lower()=="evade":
    choiceevade=input("Racked")
else: print("") 
if choicestairs not in("run","fight", "evade"):
    print("I'm sorry, but that wasn't one of the designed options, please type in one of the words that are in all caps, or maybe you might get lucky in picking something not in caps, who knows? But seriously, just pick one of the all caps words, you need to get lucky to find the secrets.")

#Second Choice Left Responses
if choiceleft.lower()=="grab":
    choicegrab=input("A")
elif choiceleft.lower()=="look":
    choicelook=input("B")
elif choiceleft.lower()=="eating":
    choiceeating=input("C")
if choicestairs not in("grab","look", "eating"):
    print("I'm sorry, but that wasn't one of the designed options, please type in one of the words that are in all caps, or maybe you might get lucky in picking something not in caps, who knows? But seriously, just pick one of the all caps words, you need to get lucky to find the secrets.")


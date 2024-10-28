height1=input("What's your height? In inches?")
age1=input("What's your age?")
number_of_riders=input("Are you riding with someone else?")
if number_of_riders.lower()=="yes":
    height2=input("What is their height, in inches?")
    age2=input("What is their age?")
    if height1<36:
        print("I am sorry, but you cannot ride. You're just too short. Come back next time!")
    if height1>=36 and height1<62:
        if height2>=62 and age2>=18:
            print("Congradulations! You can ride! Enjoy your trip and be safe!")
        if height2<62 or age2<18:
            print("I'm sorry, but you cannot ride. Your partner doesn't meet qualifications, if you come back with someone at least 18 and 5' 2'', and we'd be glad to let you ride though!")
    if height1>=62 and age1>=18:
        if height2<36:
            print("You may ride, but your partner may not. Either ride alone, or find someone a bit taller.")
        if height2>=36:
            print("Congradulations! You can ride! Enjoy your trip and be safe!")
    if age1<18 and age2<18:
        if age1>=12 and age2>=12 and height1>=52 and height2>=52:
            print("Congradulations! You can ride! Enjoy your trip and be safe!")
        if age1<12 or age2<12 or height1<52 or height2<52:
                    print("I am sorry, but you cannot ride.")
    if age


if number_of_riders.lower()=="no":
        if height1>=62 and age1>=18:
            print("Congradulations! You can ride! Enjoy your trip and be safe!")
        if height1<62 or height1<18:
            print("I am sorry, but you cannot ride alone. If you come back with an adult you may though!")


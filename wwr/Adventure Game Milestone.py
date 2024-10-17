choiceleft=""
choicegrab=""
choicestairs=""
choiceeating=""
runningaway=""
choicerun=""
choiceeat=""
choiceright=""
pet=""
drink=""
tackle=""



choiceone=input("You wake up feeling very groggy, with a splitting headache and blurry vision. As it clears, you find yourself within a dimly lit mansion. Its the middle of the night, and you hear sounds of a storm outside. The mansion is eerily silent, with only a dozen candles to light your view. You seem to be in the entry room of the mansion, with a staircase leading to a second floor, a door to the right and left, and a set of double doors on the far wall. Do you go up the STAIRS, to the LEFT, or to the RIGHT?")
#First Choice Responses
if choiceone.lower()=="left":
    choiceleft=input("You choose the left door, and find yourself in the dining room, a large rectangular table stretches out before you, filled with surprisingly warm and fresh food of all kinds. Turkey, sausage, beef, potatoes, carrots, and rolls. Near the end of the table, there was also a small array of desserts, some cookies and cakes and such. You gratefully dig in, as you realize how hungry you are. In the middle of eating, you hear a loud bang come from under the table. Do you either, LOOK under the table, GRAB some food for the road and go, or simply continue EATING?")
elif choiceone.lower()=="stairs":
    choicestairs=input("You stand up, gathering yourself, and begin to move your way up the stairs, as you do, the boards creak beneath your feet. About midway up, a cold wind blows through a broken window, which chills you to the bone. As you look up to the window, you see something else blew in as well. A large bat, flies in, shrieking and screaming. Do you try to FIGHT the bat, do you RUN away, or do you EVADE the bat, and keep climbing the stairs?")
elif choiceone.lower()=="right":
    choiceright=input("You choose the right door. It leads outside to a large courtyard. In the center of the courtyard is a large, old fountain, spewing water. As you get closer, you notice the subsatance is thicker than water, but just as clear. As you peer into the substance you see a massive toad resting underwater, in the bottom of the fountain. Do you DRINK some of the liquid, or PET the frog?")  
elif choiceone.lower() in("leave","double doors","doors"):
    secondchoice=input("You try the double doors, and notice they are unlocked. You open them to find an exit to the mansion. You leave, and by the light of the moon, manage to find your way home without any further incedent. You have WON! And you found the secret ending!")
    end=input("Click Enter to End the Program")
    if end=="": quit()
    else: quit()
    #Second Choice Responses
if choicestairs.lower()=="run":
    choicerun=input("Hassen")
elif choicestairs.lower()=="fight":
    choicefight=input("Pie")
elif choicestairs.lower()=="evade":
    choiceevade=input("Racked")
if choiceleft.lower()=="grab":
            choicegrab=input('You grab some food, and run as fast as you can, as you do, you hear a louder sound behind you, and a deep voice shout "PUT THAT BACK!". Do you TURN around, keep RUNNING, or EAT the food as fast as you can?')
if choicegrab.lower()=="eat":
      choiceeat=input("Strudel")
if choicegrab.lower()=="turn":
      print("Hello")
if choicegrab.lower()=="running": 
      runningaway=input("Hi")

elif choiceleft.lower()=="look":
    choicelook=input("sadf")
elif choiceleft.lower()=="eating":
    choiceeating=input("C")


#Right Path Choices
if pet.lower()=="tackle":
         input("You tackle the toad as it leaps at you, but as you do so, the toad opens its mouth as wide as it can. Unable to alter your course now that you've left the ground, you slide right into his stomach, and the toad has lunch thanks to you. Sorry, you lose.")
         end=input("Click Enter to End the Program")
         if end=="": quit()
         else: quit()
if pet.lower()=="dodge":
        input("You successfully dodge out of the way of the toad, but in so doing, you fall into the water. Soaked in it now, you feel yourself shrinking. Getting smaller and smaller, until the toad towers over you, licking its lips. Looks like your time is up. Sorry, you lose.")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()
if choiceright.lower()=="drink":
         drink=input("Careful not to bother the toad, you scoop up the liquid in your cupped hands, and drink it. Your vision begins to blur, and as you look down at yourself, you don't see yourself. You've become invisible! As you walk throughout the courtyard, you come to what looks like an exit, but there's a guard patrolling the exit. Do you try to SNEAK past him, TRICK him, or TALK to him?")
if drink.lower()=="talk":
      input('You walk up to the guard, and say hi. The guard is spooked, and looks around to find the source of the voice. "I am right here!", you say, tapping the guard on the shoulder. The guard notices you and says, "What are you?" "That does not really matter," you say, "I just want to go home, can you let me out?" The guard ponders this for a while, before conceding, "I guess" he says, before moving to the side and letting you out. You run as fast as you can out of the mansion'+"'s grounds. You've made it out! You WON!")
      end=input("Click Enter to End the Program")
      if end=="": quit()
      else: quit()
if drink.lower()=="trick":
      input("You decide to trick the guard, and stealthily pick up a stone, while outside the guard's view. you throw the rock, as hard as you can. It makes a loud clatter as it falls, alerting the guard. He leaves his post to go investigate the sound. While he's gone, you run as fast as you can, and you make it out. You're free! You've WON!")
      end=input("Click Enter to End the Program")
      if end=="": quit()
      else: quit()
if drink.lower()=="sneak":
    input("You decide you want to sneak past the guard. You make yourself as thin as possible, and attempt to sqeeze past him. Unfortunately, the guard rests his hand on the wall, or rather, what he thought was a wall. He really put his hand on your face! Feeling an invisible being, the guard is shocked, and swings his sword wildly, afraid that whatever he grabbed was dangerous. He didn't know that he was really ending any chance you had of escape. You've LOST, sorry.")
    end=input("Click Enter to End the Program")
    if end=="": quit()
    else: quit()
else: 
    print("I'm sorry, but that wasn't one of the designed options, please type in one of the words that are in all caps, or maybe you might get lucky in picking something not in caps, who knows? But seriously, just pick one of the all caps words, you need to get lucky to find the secrets.") 


input("Click Enter to End the Program")

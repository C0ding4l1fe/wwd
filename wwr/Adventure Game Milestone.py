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
eating=""
follow=""


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
#Stairs Choice Responses
if choicestairs.lower()=="run":
    choicerun=input("Hassen")
elif choicestairs.lower()=="fight":
    choicefight=input("Pie")
elif choicestairs.lower()=="evade":
    choiceevade=input("Racked")

#Left Choice Responses
elif choiceleft.lower()=="look":
    choicelook=input("You look under the table to see a woman in armor, climbing down a pit under the table. She doesn't notice you as he leaves to who knows where. Do you FOLLOW her, or IGNORE her?")
    if choicelook.lower()=="ignore":
        input("You ignore the woman, lower the tablecloth, and continue to eat contentedly, as you do, you begin to feel even more tired, and fall asleep on the table. When you wake, you are no longer in the dining room, and are tied to a chair. A very angry man is sitting in front of you. He berates you for eating his food, and asks you for an explanation. Do you LIE, or tell the TRUTH?")
    if eating.lower()=="truth":
        input("You decide to tell the truth. You explain how you don't know how you got here, and just want to get home. You were hungry, and saw the abandoned food and figured it wouldn't hurt anything to eat some of it. The man's face shifts from anger to pity. He frees you from the chair, and says he'll help you get home. He leads you out of the mansion, where a team of horses are waiting, attached to a carriage. You give him the directions to your house, and in about 15 minutes, you are safe at home. You thank the man as he speeds away, and he smiles and waves goodbye, speeding into the night. You still don't know how you got in the mansion, and rightfully you don't want to. You're just glad to be home. You've WON!")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()
    if eating.lower()=="lie":
        input('You decide to lie. You say you thought the food was for you, and that you are insulted by his accusations. You try to pull the "Do you know who I am!?" card, but nothing seems to be working. The man seems to get angrier with every word you say, until eventually, he silences you, and says with a snarl, "I am the lord of this castle, and you will stay here, until you learn respect, you vile thief!" The man stood up, walks behind you. You hear a thud and a locking mechanism. He seems to have left you trapped in here, with no means of escape. I'"'m sorry, you've LOST!")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()")
    
    
    
    
    
    if choicelook.lower()=="follow":
        follow=input("You decide to follow her down the pit, climbing down the ladder a short while after she's gone. You reach the bottom, and the woman is gone. You find yourself in an underground tunnel, do you go FORWARD, or BACKWARD from the ladder?")
    if follow.lower()=="forward":
        forward=input("You decide to move forward, travelling down the tunnel for a long time, passing by many offshoots and tunnels. The tunnel is very dimly lit, lit only by the occasional torch. After a while, you begin to feel lost. You've past far beyond what you think the grounds of the mansion should be, but haven't seen any sign of escape. Just as you begin to give up hope, you see some natural light shining down from a patch of the ceiling. Eagerly, you run forward, and find a ladder, leading up to a sewer grate. you climb the ladder, push with all your might, and manage to remove the grate. You climb out of the tunnel, replace the grate, and look around. You recognize this place! Your in a field not far from your home! You begin to walk towards home, grateful to be safe and sound." '"Who knows what happened to that lady," you whisper to yourself as you walk, but you stop worrying about it after a while. If your lucky, you won'"'t have to worry about anything that happened tonight for a long time. You've WON!")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()
    if follow.lower()=="backward":
        backward=input("You decide to move backward from the ladder, and notice yourself going deeper and deeper farther down. You're not sure if that's the right way to go, but continue regardless. You also feel water beginning to gather on the floor of the tunnel, the water level getting higher as you continue. After about an hour of walking, you notice the torches lighting the walls are out. Cautiously you move forward even further, but you slip, as you do you begin to slide along the floor, and the water begins to flow downward even further. Caught in the current, you descend faster and faster into the tunnel. You can barely see anything, but you hear a large crunching sound, like the clashing of large teeth. as the sound gets louder and louder, you get more and more frightened. Your surroundings get darker suddenly, before you hear a final CRUNCH! You've been eaten, and YOU'VE LOST!")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()
elif choiceleft.lower()=="grab":
    choicegrab=input('You grab some food, and run as fast as you can, as you do, you hear a louder sound behind you, and a deep voice shout "PUT THAT BACK!". Do you TURN around, keep RUNNING, or EAT the food as fast as you can?')
    if choicegrab.lower()=="eat":
      choiceeat=input("You eat what you grabbed, and feel very strange. you begin to feel cold, as you look down to see your own body turning to ice. Whatever that food was, its freezing you alive. You have only enough time to scream before becoming a human popsicle. YOU'VE LOST!")
      end=input("Click Enter to End the Program")
      if end=="": quit()
      else: quit()
    if choicegrab.lower()=="turn":
      turn=input("You turn around to see whatever voice gave you the command. Standing behind you is a tall knight, with black flames wreathing around its armor. You can'"'t see its eyes through the helmet. Again, the knight shouts, "I said, PUT THAT BACK!" Do you PUT THE FOOD BACK on the table, or EAT it as quickly as possible ')
      if turn.lower()=="put the food back":
        input("You decide to put the food back, and the knight simply nods contentedly, before vanishing in a puff of smoke. Now alone in the room, you decide there's not really anything you can do in this room, if you're not allowed to eat anything. You move back into the main room. Do you want to go RIGHT or up the STAIRS?")
      if turn.lower()=="eat":
        input('"Yeah right!" you say, before scarfing down the food. The knight begins to laugh a deep and gutteral laugh, as he points his finger at you. Your whole body feels very cold all of the sudden, as you realize that you'"'re literally turning to ice. You try to move, to do anything, but to no avail, in mere moments, your no more than an ice sculpture. You shouldn't have eaten that food. YOU'VE LOST!")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()
    if choicegrab.lower()=="running": 
      runningaway=input("You continue to run, ignoring whatever had called out to you. You manage to make it to the doorway, but as you cross the threshold you are hit in the back by something, hard. As you stand back up, you see your feet turn to stone. The stone creeps higher and higher, until your nothing but a statue, standing in the doorway. sorry, but YOU'VE LOST!")
      end=input("Click Enter to End the Program")
      if end=="": quit()
      else: quit()
elif choiceleft.lower()=="eating":
    eating=input("You continue to eat, and as you do, you never seem to get full. You just eat, and eat, and eat, until eventually, you're too tired to continue, and fall asleep on the table. When you wake, you are no longer in the dining room, and are tied to a chair. A very angry man is sitting in front of you. He berates you for eating his food, and asks you for an explanation. Do you LIE, or tell the TRUTH?")
    if eating.lower()=="truth":
        input("You decide to tell the truth. You explain how you don't know how you got here, and just want to get home. You were hungry, and saw the abandoned food and figured it wouldn't hurt anything to eat some of it. The man's face shifts from anger to pity. He frees you from the chair, and says he'll help you get home. He leads you out of the mansion, where a team of horses are waiting, attached to a carriage. You give him the directions to your house, and in about 15 minutes, you are safe at home. You thank the man as he speeds away, and he smiles and waves goodbye, speeding into the night. You still don't know how you got in the mansion, and rightfully you don't want to. You're just glad to be home. You've WON!")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()
    if eating.lower()=="lie":
        input('You decide to lie. You say you thought the food was for you, and that you are insulted by his accusations. You try to pull the "Do you know who I am!?" card, but nothing seems to be working. The man seems to get angrier with every word you say, until eventually, he silences you, and says with a snarl, "I am the lord of this castle, and you will stay here, until you learn respect, you vile thief!" The man stood up, walks behind you. You hear a thud and a locking mechanism. He seems to have left you trapped in here, with no means of escape. I'"'m sorry, you've LOST!")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()


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

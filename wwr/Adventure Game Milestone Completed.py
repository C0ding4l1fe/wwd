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
wiggle=""
wiggle=""
talk=""
chances=""
choiceone=input("You wake up feeling very groggy, with a splitting headache and blurry vision. As it clears, you find yourself within a dimly lit mansion. Its the middle of the night, and you hear sounds of a storm outside. The mansion is eerily silent, with only a dozen candles to light your view. You seem to be in the entry room of the mansion, with a staircase leading to a second floor, a door to the right and left, and a set of double doors on the far wall. Do you go up the STAIRS, to the LEFT, or to the RIGHT?")
#First Choice Responses
if choiceone.lower()=="left":
    choiceleft=input("You choose the left door, and find yourself in the dining room, a large rectangular table stretches out before you, filled with surprisingly warm and fresh food of all kinds. Turkey, sausage, beef, potatoes, carrots, and rolls. Near the end of the table, there was also a small array of desserts, some cookies and cakes and such. You gratefully dig in, as you realize how hungry you are. In the middle of eating, you hear a loud bang come from under the table. Do you either, LOOK under the table, GRAB some food for the road and go, or simply continue EATING?")
elif choiceone.lower()=="stairs":
    choicestairs=input("You stand up, gathering yourself, and begin to move your way up the stairs, as you do, the boards creak beneath your feet. About midway up, a cold wind blows through a broken window, which chills you to the bone. As you look up to the window, you see something else blew in as well. A large bat, flies in, shrieking and screaming. Do you try to FIGHT the bat, do you RUN away, or do you EVADE the bat, and keep climbing the stairs?")
elif choiceone.lower()=="right":
    choiceright=input("You choose the right door. It leads outside to a large courtyard. In the center of the courtyard is a large, old fountain, spewing water. As you get closer, you notice the subsatance is thicker than water, but just as clear. As you peer into the substance you see a massive toad resting underwater, in the bottom of the fountain. Do you DRINK some of the liquid, or PET the frog?")  
elif choiceone.lower() in("leave","double doors","doors"):
    print("You try the double doors, and notice they are unlocked. You open them to find an exit to the mansion. You leave, and by the light of the moon, manage to find your way home without any further incedent. You have WON! And you found the secret ending!")
    end=input("Click Enter to End the Program")
    if end=="": quit()
    else: quit()
#Stairs Choice Responses
if choicestairs.lower()=="run":
    choicerun=input("You decide to run from the bat, but as you do, it swoops down, and grabs you with its claws. Carrying you high above the floor, and out the window. The brisk night air cuts at you from all sides, as the mighty beast's wings flap above you. After flying a while, you wonder why it hasn't eaten you yet. For a brief moment, the bat gets low to the ground, as it tires. Do you WAIT, or try to WIGGLE free?")
    if choicerun.lower()=="wiggle":
        print("You decide to risk it and try to wiggle out of the bat's grasp. You do manage this, falling into the woods below. You hit the ground at the top of a tall hill, and begin to roll from the momentum. rolling faster and faster, you reach the bottom. Of a pit. At the bottom of the hill there was a ditch, a pit, that you fell in. You're not sure if it was naturally made or man made, but it doesn't matter, you're stuck, its so dark, and the pit is too deep and steep to get out. You'll have to wait for someone to help you out. I'm sorry, YOU'VE LOST!")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()
    if choicerun.lower()=="wait":
        print("You decide to wait, after all, the bat hasn't hurt you yet, he could be friendly. He flies you to a large cave in the side of a distant mountain, its very late at your arrival, and you're completely exhausted. You hear a scuttling sound, as little bats move their way towards you. The bat had brought you to its children. You fall asleep as the sun is beginning to rise, completely enfeebled by the long trip. Little did you know, that was the point. The bat needed some breakfast for its babies, and you did nicely. I'm sorry, You've LOST!")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()
elif choicestairs.lower()=="fight":
    fight=input("You decide to face the beast, charging at it letting out a battle cry. You don't care that you're unarmed, you're taking this thing down! As you draw near, the beast bears its teeth, sharp and jagged, before leaping into the air, and pouncing back down, pinning you to the floor. The bat licks its black lips as it looks down at you. Its dinnertime. Do you try to SHOVE it off, or BEG for mercy?")
    if fight.lower()=="beg":
        print("You plead with the beast to spare you. You try to appeal to its better judgement, but you realize it can't understand you. It's a bat after all. What were you thinking? Well not much now... I'm sorry, YOU'VE LOST!")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()
    if fight.lower()=="shove":
        print("You try to use your strength to shove the beast off of you, but its too big. Its huge, its massive. Its immovable, there's no use. You're too tired, you're too weak, and in a soon, you'd be too dead. I'm sorry, YOU'VE LOST!")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()
elif choicestairs.lower()=="evade":
    choiceevade=input('You duck and weave around the bat, and manage to get past it. Rushing to the door at the top of the stairs, you throw it open and leap through before slamming it shut behind you. Moments later, the bat crashes into the closed door, knocking you onto the floor. You managed to escape the bat and find yourself in a bedroom of sorts, with only the moonlight shining through the window to illuminate the scene. In a large bed in the center of the room lies a very pale man, deathly pale. With a bolt, the man rises, and stands to his feet, awakened by the bat'"'s thud against the door. He'"'s dressed in a black cloak, and as he approaches you, you, an overwhelming unpleasantness washes over you. Something about this man isn'"'t right. Do you take your CHANCES with the bat, or TALK to the man?")
    if choiceevade.lower()=="chances":
        print('You decide to take your chances with the bat rather than the creepy guy, opening the door. The bat rears its head, to strike at you, and you hold up your arm in defense. The strike never comes however. You see a bolt of red light, shoot from the man'"'s fingertips, wizzes over your head, and strikes the bat in the chest, with a wimper, it falls back, onto the banister, and then off the railing down to the first floor, landing with a mighty thud! The man saved you! You turn back to thank him and he's gone, leaving only a note behind. It reads:"'" In entering this room, and awakening me, you have agreed to be keeper of this castle for all eternity, or until a replacement can be found for you. I have been waiting 10,000 years to die. Thank you for setting me free. Good luck!" "Well, imortality and a mansion isn'"'t so bad"", you think to yourself. Better go tell your family! YOU'VE WON! Kind of...")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()
    if choiceevade.lower()=="talk":
        print("You decide to talk to the man, he can't be that bad after all."'"I hunger." He says quietly as he approaches you. Okay, maybe he is that bad. You try to open the door. The man quickly snaps his finger and the door is locked.'" You'e trapped in here with this maniac. The man gets closer and closer, revealing his fangs. He's a vampire, and he's hungry. And worse yet, it looks like you're on the menu! Maybe taking your chances with the bat would've been better after all! I'm sorry, YOU'VE LOST!")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()
#Left Choice Responses
elif choiceleft.lower()=="look":
    choicelook=input("You look under the table to see a woman in armor, climbing down a pit under the table. She doesn't notice you as he leaves to who knows where. Do you FOLLOW her, or IGNORE her?")
    if choicelook.lower()=="ignore":
        input("You ignore the woman, lower the tablecloth, and continue to eat contentedly, as you do, you begin to feel even more tired, and fall asleep on the table. When you wake, you are no longer in the dining room, and are tied to a chair. A very angry man is sitting in front of you. He berates you for eating his food, and asks you for an explanation. Do you LIE, or tell the TRUTH?")
    if eating.lower()=="truth":
        print("You decide to tell the truth. You explain how you don't know how you got here, and just want to get home. You were hungry, and saw the abandoned food and figured it wouldn't hurt anything to eat some of it. The man's face shifts from anger to pity. He frees you from the chair, and says he'll help you get home. He leads you out of the mansion, where a team of horses are waiting, attached to a carriage. You give him the directions to your house, and in about 15 minutes, you are safe at home. You thank the man as he speeds away, and he smiles and waves goodbye, speeding into the night. You still don't know how you got in the mansion, and rightfully you don't want to. You're just glad to be home. You've WON!")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()
    if eating.lower()=="lie":
        print('You decide to lie. You say you thought the food was for you, and that you are insulted by his accusations. You try to pull the "Do you know who I am!?" card, but nothing seems to be working. The man seems to get angrier with every word you say, until eventually, he silences you, and says with a snarl, "I am the lord of this castle, and you will stay here, until you learn respect, you vile thief!" The man stood up, walks behind you. You hear a thud and a locking mechanism. He seems to have left you trapped in here, with no means of escape. I'"'m sorry, you've LOST!")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()
    
    
    
    
    
    if choicelook.lower()=="follow":
        follow=input("You decide to follow her down the pit, climbing down the ladder a short while after she's gone. You reach the bottom, and the woman is gone. You find yourself in an underground tunnel, do you go FORWARD, or BACKWARD from the ladder?")
    if follow.lower()=="forward":
        print("You decide to move forward, travelling down the tunnel for a long time, passing by many offshoots and tunnels. The tunnel is very dimly lit, lit only by the occasional torch. After a while, you begin to feel lost. You've past far beyond what you think the grounds of the mansion should be, but haven't seen any sign of escape. Just as you begin to give up hope, you see some natural light shining down from a patch of the ceiling. Eagerly, you run forward, and find a ladder, leading up to a sewer grate. you climb the ladder, push with all your might, and manage to remove the grate. You climb out of the tunnel, replace the grate, and look around. You recognize this place! Your in a field not far from your home! You begin to walk towards home, grateful to be safe and sound." '"Who knows what happened to that lady," you whisper to yourself as you walk, but you stop worrying about it after a while. If your lucky, you won'"'t have to worry about anything that happened tonight for a long time. You've WON!")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()
    if follow.lower()=="backward":
        print("You decide to move backward from the ladder, and notice yourself going deeper and deeper farther down. You're not sure if that's the right way to go, but continue regardless. You also feel water beginning to gather on the floor of the tunnel, the water level getting higher as you continue. After about an hour of walking, you notice the torches lighting the walls are out. Cautiously you move forward even further, but you slip, as you do you begin to slide along the floor, and the water begins to flow downward even further. Caught in the current, you descend faster and faster into the tunnel. You can barely see anything, but you hear a large crunching sound, like the clashing of large teeth. as the sound gets louder and louder, you get more and more frightened. Your surroundings get darker suddenly, before you hear a final CRUNCH! You've been eaten, and YOU'VE LOST!")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()
elif choiceleft.lower()=="grab":
    choicegrab=input('You grab some food, and run as fast as you can, as you do, you hear a louder sound behind you, and a deep voice shout "PUT THAT BACK!". Do you TURN around, keep RUNNING, or EAT the food as fast as you can?')
    if choicegrab.lower()=="eat":
      print("You eat what you grabbed, and feel very strange. you begin to feel hot, really hot, like fire, as you look down to see your own body turning to ash! Whatever that food was, its burning you alive. You have only enough time to scream before you're nothing more than  a pile of ashes on the floor to be swept up. YOU'VE LOST!")
      end=input("Click Enter to End the Program")
      if end=="": quit()
      else: quit()
    if choicegrab.lower()=="turn":
      turn=input("You turn around to see whatever voice gave you the command. Standing behind you is a tall knight, with black flames wreathing around its armor. You can'"'t see its eyes through the helmet. Again, the knight shouts, "I said, PUT THAT BACK!" Do you PUT THE FOOD BACK on the table, or EAT it as quickly as possible ')
      if turn.lower()=="put the food back":
        print('You decide to put the food back, the knight seems happy at this, nodding contentedly. "Thank you. Would you like to go home where you can eat your own food?" You nod, a bit confused at why the knight was suddenly being so nice. The knight snaps his fingers and he and you both disapear in a wisp of smoke. Seconds later, you both reappear, right outside the door to your house. "Be safe," the knight said, before walking away. You walk towards your house, but turn to ask the knight a question, "Why did you help me?", you say. The knight turns to you, his fingers ready to snap himself back to the castle, and says, "I am the keeper of that castle. You didn'"'t belong there, so I returned you to where you belonged. Simple as that."'" Then the knight snapped, and disapeared. as you walk inside, you feel the peace of home wash over you. Everything is as it should be. YOU WON!')
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()
      if turn.lower()=="eat":
        print('"Yeah right!" you say, before scarfing down the food. The knight begins to laugh a deep and gutteral laugh, as he points his finger at you. Your whole body feels very cold all of the sudden, as you realize that you'"'re literally turning to ice. You try to move, to do anything, but to no avail, in mere moments, your no more than an ice sculpture. You shouldn't have eaten that food. YOU'VE LOST!")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()
    if choicegrab.lower()=="running": 
      print("You continue to run, ignoring whatever had called out to you. You manage to make it to the doorway, but as you cross the threshold you are hit in the back by something, hard. As you stand back up, you see your feet turn to stone. The stone creeps higher and higher, until your nothing but a statue, standing in the doorway. sorry, but YOU'VE LOST!")
      end=input("Click Enter to End the Program")
      if end=="": quit()
      else: quit()
elif choiceleft.lower()=="eating":
    eating=input("You continue to eat, and as you do, you never seem to get full. You just eat, and eat, and eat, until eventually, you're too tired to continue, and fall asleep on the table. When you wake, you are no longer in the dining room, and are tied to a chair. A very angry man is sitting in front of you. He berates you for eating his food, and asks you for an explanation. Do you LIE, or tell the TRUTH?")
    if eating.lower()=="truth":
        print("You decide to tell the truth. You explain how you don't know how you got here, and just want to get home. You were hungry, and saw the abandoned food and figured it wouldn't hurt anything to eat some of it. The man's face shifts from anger to pity. He frees you from the chair, and says he'll help you get home. He leads you out of the mansion, where a team of horses are waiting, attached to a carriage. You give him the directions to your house, and in about 15 minutes, you are safe at home. You thank the man as he speeds away, and he smiles and waves goodbye, speeding into the night. You still don't know how you got in the mansion, and rightfully you don't want to. You're just glad to be home. You've WON!")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()
    if eating.lower()=="lie":
        print('You decide to lie. You say you thought the food was for you, and that you are insulted by his accusations. You try to pull the "Do you know who I am!?" card, but nothing seems to be working. The man seems to get angrier with every word you say, until eventually, he silences you, and says with a snarl, "I am the lord of this castle, and you will stay here, until you learn respect, you vile thief!" The man stood up, walks behind you. You hear a thud and a locking mechanism. He seems to have left you trapped in here, with no means of escape. I'"'m sorry, you've LOST!")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()


#Right Path Choices
if choiceright.lower()=="drink":
    drink=input("Careful not to bother the toad, you scoop up the liquid in your cupped hands, and drink it. Your vision begins to blur, and as you look down at yourself, you don't see yourself. You've become invisible! As you walk throughout the courtyard, you come to what looks like an exit, but there's a guard patrolling the exit. Do you try to SNEAK past him, TRICK him, or TALK to him?")
    if drink.lower()=="talk":
      print('You walk up to the guard, and say hi. The guard is spooked, and looks around to find the source of the voice. "I am right here!", you say, tapping the guard on the shoulder. The guard notices you and says, "What are you?" "That does not really matter," you say, "I just want to go home, can you let me out?" The guard ponders this for a while, before conceding, "I guess" he says, before moving to the side and letting you out. You run as fast as you can out of the mansion'+"'s grounds. You've made it out! You WON!")
      end=input("Click Enter to End the Program")
      if end=="": quit()
      else: quit()
    if drink.lower()=="trick":
      print("You decide to trick the guard, and stealthily pick up a stone, while outside the guard's view. you throw the rock, as hard as you can. It makes a loud clatter as it falls, alerting the guard. He leaves his post to go investigate the sound. While he's gone, you run as fast as you can, and you make it out. You're free! You've WON!")
      end=input("Click Enter to End the Program")
      if end=="": quit()
      else: quit()
    if drink.lower()=="sneak":
        print("You decide you want to sneak past the guard. You make yourself as thin as possible, and attempt to sqeeze past him. Unfortunately, the guard rests his hand on the wall, or rather, what he thought was a wall. He really put his hand on your face! Feeling an invisible being, the guard is shocked, and swings his sword wildly, afraid that whatever he grabbed was dangerous. He didn't know that he was really ending any chance you had of escape. You've LOST, sorry.")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()
if choiceright.lower()=="pet":
    pet=input("You cautiously lean over the fountain, and reach into the liquid to pet the toad. As soon as you touch it however, the frog looks at you eagerly, before bounding out at you! Do you want to TACKLE it, or DODGE out of the way?")
    if pet.lower()=="tackle":
         print("You tackle the toad as it leaps at you, but as you do so, the toad opens its mouth as wide as it can. Unable to alter your course now that you've left the ground, you slide right into his stomach, and the toad has lunch thanks to you. Sorry, you lose.")
         end=input("Click Enter to End the Program")
         if end=="": quit()
         else: quit()
    if pet.lower()=="dodge":
        print("You successfully dodge out of the way of the toad, but in so doing, you fall into the water. Soaked in it now, you feel yourself shrinking. Getting smaller and smaller, until the toad towers over you, licking its lips. Looks like your time is up. Sorry, you lose.")
        end=input("Click Enter to End the Program")
        if end=="": quit()
        else: quit()

else: 
    print("I'm sorry, but that wasn't one of the designed options, please type in one of the words that are in all caps, or maybe you might get lucky in picking something not in caps, who knows? But seriously, just pick one of the all caps words, you need to get lucky to find the secrets.") 


input("Click Enter to End the Program")

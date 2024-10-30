underscores="_ _ _ _ _"
print("Welcome to the guessing game!")

guess=input("Please make your guess!:"+underscores)
count = 0
while not guess.lower() =="alma":
        print("I'm sorry, but that's incorrect, please guess again!")
        guess=input("Please make your guess!:"+underscores)

        count+=1
print(f"Congradulations, you got it! You tried {count+1} times!")



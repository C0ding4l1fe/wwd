number=float(input("Please enter a positive number!"))
while number <0:
    print("I'm sorry, but that's a negative number, I asked for a positive one. Could you please enter a positive number?")
    number=float(input("Please enter a positive number!"))

print(f"The number is {number}!")
candy=input("Can I have some candy?")
while candy.lower()=="no":
    candy=input("Can I have some candy?")
while candy.lower()=="yes":
    print("Thank You!")
    end=input("Press Enter to End the Program")
    if end=="":
        quit()

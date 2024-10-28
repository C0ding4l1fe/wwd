number=int(input("Please enter a positive number!"))
while number <0:
    print("I'm sorry, but that's a negative number, I asked for a positive one. Could you please enter a positive number?")
    number=int(input("Please enter a positive number!"))
print("The number is {number}")
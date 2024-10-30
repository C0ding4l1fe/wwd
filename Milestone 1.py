underscores=""
def convert_to_underscores(string):
  import re
  return re.sub(r'[^a-zA-Z0-9]', '_', string)

secret_word="alma"
def convert_letter(secret_word):
    underscores = secret_word
    for i in range(0, len(secret_word)):
        if ord(secret_word[i]) != 32:
            underscores = underscores.replace(secret_word[i], '_ ')
convert_letter(secret_word)
print("Welcome to the guessing game!")
guess=input("Please make your guess!:"+underscores)
count = 0
while not guess.lower() =="alma":
        print("I'm sorry, but that's incorrect, please guess again!")
        guess=input("Please make your guess!:")

        count+=1
print(f"Congradulations, you got it! You tried {count+1} times!")



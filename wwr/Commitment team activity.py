capital=input("What's your favorite letter in the word commitment?")
commitment="commitment"
for letters in commitment:
  if letters==capital.lower():
    letters="_"
  print(letters,end="")
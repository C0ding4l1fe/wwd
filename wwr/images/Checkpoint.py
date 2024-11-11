friend_name=""
friend_list= [friend_name]

while friend_name.lower() !="end":
  friend_name=input("Type the name of a friend:")
  if friend_name.lower()!="end":
    friend_list.append(friend_name)
print("The names of your friends are:")
for friend_name in friend_list:
  print(friend_name.capitalize())
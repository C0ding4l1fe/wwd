choice=""
add=""
shopping_list=[""]
print("Hello! Welcome to the digital shopping cart!")
while choice!=5:
  print("Please select one of the following below:")
  print("1. Add item to cart")
  print("2. View cart")
  print("3. Remove from cart")
  print("4. Calculate total of cart contents")
  print("5. Quit")
  choice=int(input("Please input your choice, by the number:"))
  if choice==1:
    add=input("What would you like to add?:")
    shopping_list.append(add)
    print(f"Alright! {add.capitalize()} has been added to your shopping list!")
  if choice==2:
    print("Alright! Here are the items in your cart so far!:")
    print(shopping_list)
print("Okay then, we'll see you next time!")
  
count=0
remove=""
import time
choice=""
add=""
price_list=[]
shopping_list=[add]
shopping_list.remove("")
real_total=0
price=0

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
    price_ask=float(input("What's the price of that item?:"))
    price==float(round(price_ask,2))
    price_list.append(price)
    print(price_list)
    shopping_list.append(add)
    print(f"Alright! '{add.capitalize()}' has been added to your shopping list!")
    time.sleep(1)

  elif choice==2:
    print("Alright! Here are the items in your cart so far!:")
    for add in shopping_list:
      count+=1
      print(f"{str(count)}. {add} - ${price: .2f}".capitalize())
    print("")
    time.sleep(1)
  elif choice==3:
    remove=input("What item you like to remove?:")
    shopping_list.remove(remove)
    print(f"Alrighty! '{remove.capitalize()}' has been removed from the list!")
    time.sleep(1)
  elif choice==4:
    print("Here's your total cost so far!:")
    total=0
    for price in price_list:
      real_total==total+price
    print(f"${real_total:.2f}")

  



print("Okay then, we'll see you next time!")
  

childmeal=float(input("What's the cost of a child's meal at the restaraunt?: "))
adultmeal=float(input("What's the cost of an adult's meal at the restaraunt?: "))
drink=float(input("What's the cost of each drink for your group?: "))
side=float(input("What's the cost of each side dish?: "))
child=int(input("How many kids are here?: "))
adult=int(input("How many adults are here?: "))
childcost=int (childmeal*child)
adultcost=int(adult*adultmeal)
drinkcost=float((adult+child)*drink)
sidecost=float((adult+child)*side)
taxes=float(input("What's the current sales tax rate?: "))
subtotal=float(childcost+adultcost+sidecost+drinkcost)
print ("Subtotal: $"+str(subtotal))
tax=float (round((taxes/100),2))
salestax=float(subtotal*tax)
saletax=round(salestax,2)
print ("Sales Tax: $"+str(saletax))
cost=float(subtotal+saletax)
print ("Total Cost: $" +str(cost))
payment=float(input("How much are you gonna pay?"))
change=float(payment-cost)
totalchange=round(change,2)
print("Change: $" +str(totalchange))
input("Click Enter to End the Program")


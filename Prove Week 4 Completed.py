
#Questions:
child_meal=float(input("What's the cost of a child's meal at the restaraunt?: "))
adult_meal=float(input("What's the cost of an adult's meal at the restaraunt?: "))
drink=float(input("What's the cost of each drink for your group?: "))
side=float(input("What's the cost of each side dish?: "))
child=int(input("How many kids are here?: "))
adult=int(input("How many adults are here?: "))
taxes=float(input("What's the current sales tax rate?: "))

#Cost Variables
child_cost=float (child_meal*child)
adult_cost=float(adult*adult_meal)
drink_cost=float((adult+child)*drink)
side_cost=float((adult+child)*side)
subtotal=float(child_cost+adult_cost+side_cost+drink_cost)
Real_Subtotal=round(subtotal,2)
print (f"Subtotal: ${Real_Subtotal}")

#Taxes Codes
tax=float (round((taxes/100),2))
sales_tax=float(Real_Subtotal*tax)
sale_tax=round(sales_tax,2)
print (f"Sales Tax: ${sale_tax}")

#Ending Calculations and Displays
#Cost
cost=float(Real_Subtotal+sale_tax)
total_cost=round(cost,2)
print (f"Total Cost: ${total_cost}" )

#Payment and Change 
payment=float(input("How much are you gonna pay?"))
change=float(payment-total_cost)
total_change=round(change,2)
print(f"Change: ${total_change}")

#Prevent from Closing Code
input("Click Enter to End the Program")


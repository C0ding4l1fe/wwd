number=21
number_list=[]
count=0
print("Enter a list of numbers, type 0 when you're done.")
while number !=0:
  count+=1
  number=float(input("Enter a number: "))
  number_list.append(number)

largest = -100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
smallest=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
for number in number_list:
  if number >=0:  
    if number < smallest:

        smallest = number


for number in number_list:

    if number > largest:

        largest = number

print(f"The sum of your numbers is:{sum(number_list)}")
print(f"The average of your numbers is:{(sum(number_list))/(count-1)}")
print(f"The largest is {largest}")
print(f"The smallest positive number is {smallest}")


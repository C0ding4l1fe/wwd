print("Rate yourself on a scale of 1 to 10 on the following questions, and we'll tell you if you're being financially responsible:")
loan=float(input("How large is your loan?"))
credit=float(input("How good is your credit history?"))
income=float(input("How high is your current salary?"))
down_payment=float(input("How big is your down payment on your loan?"))
print("Thank you! Now calculating data. Please wait.")
import time
time.sleep(3)
print("Data Assembled, see below!")
print("------------------------------------------------")
if loan >= 5:
    if credit >=7 and income>=7:
        print("Yes, this is a financially sound loan. You should be fine.")
    if credit >=7 or income>=7:
        if down_payment>=5:
            print("Yes, this is a financially sound loan. You should do well in paying it back.")
        if down_payment<5:
            print("No, this is not a financially responsible descision. Wait to take out the loan until you can either pay a bigger down payment, have a better income, or a better credit score.")
    if credit <7 and income <7:
            print("No, this is not a financially responsible descision. Wait to take out the loan until your income or credit score has increased")
if loan<5:
    if credit<4:
        print("No, you need to wait until you have a better credit score before making this loan.")
    if credit>=4:
        if income>=7 or down_payment>=7:
            print("Yes, this is a financially sound loan. You should do well in paying it back.")
        elif income>=4 and down_payment>=4:
            print("Yes, this is a financially sound loan. You should do well in paying it back.")
        elif income<4 or down_payment<4:
            print("No, you need to wait until you have a higher income, or pay a bigger down payment, before making this loan.")
 
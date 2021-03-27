#!/usr/bin/python3

print("Welcome to TIP Calculator")

bill = float(input("Enter the Total Bill Amount: "))
tip_percent = float(input("Enter the percentage of Tip to give: "))
no_of_people = int(input("Enter the number of people to split the bill with: "))


total_bill = bill + ( (bill * tip_percent)/100 )
split_per_head = round(total_bill / no_of_people)

#Formatting the amount to 2 Decimal places precision
print("Amount payable per person is: " + "{:.2f}".format(split_per_head))
#!/usr/bin/python3

# Formula: weight (kg) / [height (m)]^2


print("Welcome to BMI Calculator")

height = float(input("Enter your height in metres:\n"))
weight = float(input("Enter your weight in Kgs:\n"))


bmi = round( weight / (height ** 2) ,2 )

print(f"Your Body Mass Index is: {bmi}")
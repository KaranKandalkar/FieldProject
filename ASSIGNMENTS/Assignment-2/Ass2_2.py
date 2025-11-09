# Q2. Write a program to input three numbers and find the greatest among them. (if-else)

# Input numbers
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

# Conditions and result
if num1 > num2:
    print(f"The greater number is :- {num1}")
elif num2 > num3:
    print(f"The greater number is :- {num2}")
else:
    print(f"The greater number is :- {num3}")
# Q7. Write a program to input a number and display the same number in hexadecimal and binary format

# Input a number for converting
num = int(input("Enter a number:-"))

# Calculation 
binary = bin(num) [2:]
hexadecimal = hex(num) [2:].upper()

# Display result
print(f"The binary number is = {binary} \nThe hexadecimal number = {hexadecimal}")
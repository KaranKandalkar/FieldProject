# Q8. Write a program to find the factorial of a number using a loop.

# Input number
num = int(input("Enter a number: "))

factorial = 1

# For loop statement
for i in range(1, num + 1):
    factorial *= i   

print(f"The factorial of {num} is {factorial}")

# Q5. Write a program to input an integer and check whether it is positive, negative, or zero. (if-else)

# Input integer
num = int(input("Enter a number: "))

# Conditions and results
if num == 0:
    print("The given number is zero....")
elif num > 0:
    print("The given number is positive.")
else:
    print("The given number is negative.")
# Q10. Write a program to reverse a given number using a loop.

# Input number
num = int(input("Enter a number: "))
reverse = 0 #initialize a variable

# while loop statement
while num > 0:
    digit = num % 10        
    reverse = reverse * 10 + digit
    num = num // 10         

# Display result
print(f"Reversed number is: {reverse}")

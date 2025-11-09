# Q7. Write a program to print the multiplication table of a number using a loop.

# Input number
num = int(input("Enter a number : "))

# Type 1 - For loop statement
for i in range(1,11):
    print(f"{num} * {i} = {num * i}")

print()
# Type 2 - While loop statement
n = 1
while  n<=10:
    print(f"{num} * {n} = {num * n}")
    n+=1
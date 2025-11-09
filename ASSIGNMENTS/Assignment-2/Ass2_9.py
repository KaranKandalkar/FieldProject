# Q9. Write a program to display the sum of all even numbers between 1 and 50 using a loop.

# Initialization 
sum = 0

# For loop statement
for i in range(1,51):
    if i % 2 == 0: #check the number is even or not
        sum+=i 

# Display result
print("The sum of all even numbers from 1-50 is = " ,sum)
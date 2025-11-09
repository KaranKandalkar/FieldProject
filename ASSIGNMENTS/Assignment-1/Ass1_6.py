# Q6. Write a program to input the principal, rate, and time, and display the simple interest

# Input principal, rate and time
p = float(input("Enter principal ammount:- "))
r = float(input("Enter rate of interest:- "))
t = float(input("Enter time in years:- "))

# Calculations
SI = (p * r * t) / 100

# Display result
print("\nThe simple interest is = " ,SI)



# Total ammount 
# print("\nThe total ammount is = " ,p + SI)
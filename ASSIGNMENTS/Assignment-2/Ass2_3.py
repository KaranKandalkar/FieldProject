# Q3. Write a program to input a year and check whether it is a leap year or not. (if-else)

# Input year
year = int(input("Enter the year :"))

# Condition and result
if year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
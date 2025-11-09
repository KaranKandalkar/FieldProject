# Q4. Write a program to input the radius of a circle and display its area and circumference.

# Input radius
rad = float(input("Enter the radius :- "))

# Calculations
area = 3.14 * rad * rad
circumference = 2 * 3.14 * rad

print("The area of circle is = {:.2f} \nThe circumference of circle is = {:.2f}".format(area,circumference))
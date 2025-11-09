# Q5. Write a program to input temperature in Celsius and convert it into Fahrenheit.

# Input temperature
temp = int(input("Enter temperature in celcius :- "))

# Calculation
f = (temp * (9/5)) + 32

# Display Result
print(f"{temp} degree celcius= {f} farenheit")
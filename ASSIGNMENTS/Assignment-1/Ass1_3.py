# Q3. Write a program to input the marks of 5 subjects and display the total and average marks.

# Message
print("Enter your marks as per the subject ")
# Input for marks
sub1 = int(input("English:- "))
sub2 = int(input("Math:- "))
sub3 = int(input("Physics:- "))
sub4 = int(input("Chemistry:- "))
sub5 = int(input("Biology:- "))

# Calculations
total = sub1 + sub2 + sub3 + sub4 + sub5
avg = (sub1 + sub2 + sub3 + sub4 + sub5)/5

# Display Result
print("\nTotal marks obtained = {} \nAverage of marks  = {}".format(total,avg))
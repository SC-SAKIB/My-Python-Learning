#This is my second python program 
#Assingment Operators
num = 10
num **= 10
print("num :",num)
#Logical Operators
a = int("50")
b = 30.5
print(not False)
print(not(a>b))
print("And operator:", (a==b) and (a>b))#{False} If one value is False then result will be False. 
print("OR Operator", (a==b) or (a>b))# {True} If one value is True then result will be True. 
#Type Conversion: It automatically changes variables type and do the operation
sum=(a+b)
print(sum)
#type casting : Here manually forced and changed
# a = "50"
# b=30.5 
print(type(a))
print(a+b)
#**Input in Python : input() statement is used to accept values ( using keyboard) from user

#PRACTICE
# 1)write a program to input two numbers and print their sum.
#a=int(input("Enter number a="))
#b=int(input("Enter number b="))
#print(("sum ="),a+b)
# 2)PRACTICE:WRITE A PROGRAM TO INPUT SIDCE OF A SQUARE AND PRINT ITS AREA.
#side=float(input("a="))
#print("Area =",side**2)
# 3) PRACTICE: WAP TO INPUT 2 FLOATING POINT NUMBERS AND PRINT THEIR AVERAGE.
#WAP TO INPUT 2 INT NUMBERS a and b print True if a is great than or equal to b . If not print False
a=int(input("Enter 1st Number="))
b=int(input("Enter 2nd Number="))
print(a>=b)




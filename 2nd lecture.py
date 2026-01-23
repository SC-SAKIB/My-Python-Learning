#Escape sequence character.#concatenation operation
str1="Sakib"
str2="Hossain"
Final_str=str1+str2
print("Final_str:",Final_str)
#Length of strings
str="I am working as a Procurement Admin in Efficient Software Solutions"
print(len(str))
#Indexing (Identify the position number)
print(str[1])
#Slicing (Important for ML): Accessing parts of a string
chars="Sakib Hossain"
print(chars[2:])
#Negative Index
name="apple"
print(name[-5:-1])
#String Functions
name="apple"
print(name.endswith("eng"))
#capitalize
print(name.capitalize())
name=name.capitalize()
print(name)
#Replace
print(name.replace("pp","rr"))
#find
print(str.find("Procurement"))
#Count
print(str.count("s"))
#Practice Questions and solution
#
#2 Ocuuracne of $
money="2$lfjadf$afjna$ngoasnf"
print(money.count("$"))
#Conditional Statements (if, elif, else-syntax)
age=16
if(age>=18):
    print("Can Vote")
elif(age<18):
    print("Can not vote")    
marks=int(input("Marks of the student="))
if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"   
else:
    grade="D"
print("Grade of the student:",grade) 

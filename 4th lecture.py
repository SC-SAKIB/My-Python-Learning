#Dictionary and sets
info = {
    "name" : "sakib",
    "age" : 25,
    "Subjects" : {
        "Physics" : 97,
        "math" : 85,
        "English" : 80
    }
}   
info["Subjects"].update({"Bangla": 75})
print(info) 

#Set in python
Credentials = {1,2,3,4,4,"sakib", "maruf",6 }
Credentials.add ("ESS")
Credentials.add((1,2))
print(Credentials)
print(len((Credentials)))
#set methods
set1={1,2,3}
set2={2,3}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1)
print(set2)
#practice question
dic={
    "cat":"a small animal",
    "table":["a piece of furniture","lsit of facts & figures"]
}
print(dic)
#2)
Subjects={"python","javascripts","c++","java","python","java","python","java","c++","c"}
print(len(Subjects))
#3)
marks={}
x=int(input("Enter number="))
marks.update({"phy":x})
x=int(input("Enter number="))
marks.update({"math":x})
x=int(input("Enter number="))
marks.update({"chem":x})
print(marks)
#3)
values={9,"9.0"} #solution 1
print(values)
#solution2-built in data type
Creden={
    ("int",9),
    ("float",9.0)
}
print(Creden)




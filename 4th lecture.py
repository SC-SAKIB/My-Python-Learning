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



#nesting
#practice
 
#2)
#a=float(input("a="))
# b=float(input("b="))
# c=float(input("c="))
# d=float(input("d="))
# if(a>=b and a>=c and a>=d):
#     print("a is the greatest")
# elif(b>=c and b>=d):
#     print("b is the greatest")
# elif(c>=d):
#     print("c is the greatest")
# else:
#     print("d is the greatest")
#practice=3
# if((a%7)==0):
#     print("Multiple of 7")
# else:
#     print("Not a multiple of 7")
#List
student=["sakib",84.5,25,"English"]
print(type(student))
student[0]=("Ratul") #List is Mutable - It can be changed 
print(student[0])
#List Methods
list=[14,5,7,6,8]
list.append(18)
list.sort()
print(list)
list.sort(reverse=True)   
print(list)
list.reverse()
print(list)
sakib=[2,5,8,10]
sakib.insert(2,9)#specific index insert 
print(sakib)
tup=(1,2,3,2,2,"ankit")
print(tup)
print(tup.index(3))
print(tup.count(2))
#problem solve
movie1=input("1st movie:")
movie2=input("2nd mvoie:")
movie3=input("3rd mvoie:")
movie_list=[movie1,movie2,movie3]
print(movie_list)
#second method
movie=[]
movie.append(input("1st"))
movie.append(input("2nd"))
movie.append(input("3rd"))
print(movie)
#3rd one : palindrome
phone1=[1,2,3,4]
phone2=[1,2,1]
copy_phone1=phone1.copy()
copy_phone2=phone2.copy()
copy_phone1.reverse()
if(phone1==copy_phone1):
    print("palindrome")
else:
    print("Not Palindrome")

    







 



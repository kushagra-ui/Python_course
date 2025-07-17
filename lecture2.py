'''Strings '''
# string operation
str="kushagra"
str2 = "jaiswal"
print(str + " " +str2)
# len
print(len(str2))

# Indexing
str_1= "Kushagra Jaiswal"
print(str_1[9])
# Slicing
a="kushagra"
print(a[0:len(a)])
print(a[:7])

# negative Index
str1="Apple"
print(str1[-5:])
#  String Functions
str_9 = "i am a coder"
print(str_9.endswith("er"))
print(str_9.capitalize())
print(str_9.replace("coder","microsoft"))
print(str_9.find("am"))
print(str_9.count("a"))
# Practice Problem
user_name=input("Enter ur name :")
print(len(user_name))
# problem2
dollar = "the Currency of usa is $. And I have 360k$ in my bank account."
print(dollar.count("$"))
# Conditional Statement

marks = int(input("Enter ur marks : "))
if (marks>=90):
    print("grade A")
elif(90>marks>=80):
    print("grade B")    
elif(80>marks>=70):
    print("grade C")
else:
    print("grade D")    

# practice 1
num = int(input("enter a number :"))
if (num%2==0):
    print("Even")
else:
    print("Odd")
# problem2 
num1 = int(input("enter a number :"))    
num2 = int(input("enter a number :"))    
num3 = int(input("enter a number :"))    

if (num1>num2 and num1>num3):
    print(num1)
elif(num2>num3):
    print(num2)
else:
    print(num3)    
# problem3
number = int(input("Give input : "))
if (number%7 == 0):
    print("multiple of 7")
else:
    print("not a multiple of 7") 
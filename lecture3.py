# list in python
marks=[89,97,43,21,56.4]
print(marks)
print(type(marks))
print(marks[2])
print(len(marks))
marks[0]=98
print(marks)
# list slicing
marks_2=[89,67,99,20,39]
print(marks_2[0:5])

# list methods
list=[2,4,6,7,89,100]
list.append(8)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
list.insert(0, 0)
print(list)
list.remove(100)
print(list)
list.pop(2)
print(list)

# Tuple in python
tup = (1,4,3,22)
print(type(tup))
print(tup[3])
# tuple method
tuple= (1,12,11,3,2,4)
print(tuple.index(12))
print(tuple.count(2))

# problem 1
movies=[]
m1 = input("enter 1st movie :")
m2 = input("enter 2nd movie :")
m3 =input("enter 3rd movie :")

movies.append(m1)
movies.append(m2)
movies.append(m3)
print(movies)

# problem 2
list_1 = ["m","a","a","m","p"]

list_copy=list_1.copy()
list_copy.reverse()

if(list_copy==list_1):
    print("palindrome")
else:
    print("not palindrome")


# problem 3

 



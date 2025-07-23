#   while loop in python
count=1
while count<=5:
     print("kushagra")
     count+=1
print(count)


'''for
      loop
          in
            python'''

num=[1,4,9,16,25,36,49,64,81,100]
x=49
idx=0
for el in num:
    if(el==x):
        print("number found at idx",idx)
    idx+=1
    


for i in range(1,101):
    print(i)

for i in range(100,0,-1):
    print(i)
    

n= int(input("enter a number :"))
for i in range(1,11):
    print(n*i)

# q1
n=int(input("Enter a number :"))

fact=1
i=1
while i <=n:
    fact *= i 
    i += 1 


print("Factorial is ",fact)


# q2
n=int(input("Enter a number :"))
factorial =1
for i in range(1,n+1):
    factorial*=i
print("factorial =",factorial)    

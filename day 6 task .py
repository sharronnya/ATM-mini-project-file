#1) write a python program that calculates and prints sum of quares numbers using 1to 5 using for loop
sum = 0
for i in range(1,6):
    sum = sum + (i ** 2)
    print("sum of squares from 1 to 5 is:", sum)

#2)write a python program that uses a while loop to print a countdown from 5 to 1
count=5
while count>0:
    print(count)
    count-=1  

#3)multpilication table  with for nested forloop write a python program 
num = int(input("enter a number:"))
for i in range(1,4):
    for j in range(1,11):
        print(num, "x" , j, "=" , num * j)

#4) write a python program that uses for loop sum of all even numbers between 0 and 10
# 
sum = 0
for i in range(0,11):
    if i % 2 == 0:
        print(i)
        sum = sum + i
        print("sum of even numbers is:", sum) 

#5)display numbers from  10 to 1 using for loop
for i in range(10,0, -1):
    print(i)  

#6)calculate sum of all numbers to from 1 to a given  number
num = int(input("enter a number:"))
sum = 0
for i in range(1,num + 1):
    sum = sum + i
    print("sum is:", sum)

#7)display a numbers from a using loop
numbers = [20,30,40,50]
for i in numbers:
    print(i)    

#8) write a python program to print the cube of all numbers from 1to given number
num = int(input("enter a number:"))
for i in range(1, num + 1):
    print("cube of", i, "is", i ** 3)
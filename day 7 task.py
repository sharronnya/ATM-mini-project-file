#1) write a python program that takes a list of numbersas input numbetrs=[25,30,20,40.15,25]print sum of the num
#sum exceeds 100 stop adding numbers print"sum exceeded 100"
numbers = [25,30,20,40,15,25]
total = 0
for i in numbers:
    total += i
    if total > 100:
        print("sum exceeded 100")
        break
print(total)

#2)write a python program script for loop iterate thruogh mnumbers from 1 to 600 
#print only the odd numbers skipping the even numbers
for i in range(601):
    if i % 2 == 0:
        continue
    print(i)

#3)write a python script that checks if a number is even or odd print
# even if odd do nothing use the pass statement
# 
num = int(input("enter the number:"))

if num % 2 == 0:
    print("even")
else:
    pass        

#4)write python script that iterates through a list  of words if the word is break
#exit the loop using the bfreak statement
#if the word is skip skip the rest of the code
#for the current iteration using the continue statement for any other word print the word

my_list = ["saranya","sai","skip","vinay","break","world"]

for i in my_list:
    if i == "skip":
        continue
    elif i == "break":
        break
    print(i)
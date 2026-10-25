

voter_data = {"kiran","saranya","vijay","madhu","sai"}
for item in voter_data:
    print(f"you'r voter is is valid")
    print(F"{item} voter id is valid")

sample = "pythonlife"
for i in sample:
    print(i)

# syntax
# range(stop)
# range(start,stop)
# range(start, stop, step)

# 0-10 seq of number generate (range() function)
for i in range(10):
    print(i)


for i in range(1,11):
    print(i)

for i in range(1,11,1):
    print(i)

for i in range(9,1001,3):
    print(i)

# multiplication of tables
for i in range(1,11):
    print(i)

for i in range(1,11):
    print(F"2 x {i}  = {2*i}")

for i in range(1,11):
    print(f"17 x {i} = {17*i}")  

table = int(input("enter the table:"))
for i in range(1,11):
    print(f"{table} x {i} = {table*i}") 

# syntax
#for i in range(3):#outer for loop
#      for j in range(3): #inner for loop
#       print(i,j)

for i in range(3):
    print(i)

for i in range(1,11):
    for j in range(1,11):
        print(i,j)

for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print()  

# syntax
# while cond:
   #bloack of code to executed


while True:
    print("welcome to pythonlife")


count = 0
while count<3:
    print(count)
    count+=1 #eq--> count = count

user_name = input("enter the username:")
password = input("enter the password:")
if user_name == "arjun" and passowrd == "arjun@123":
    print(f"ogin success....")
    print(f"welcome {user_name}")
else:
    print(f"invalid login credentials...")

# while cond:
#    while cond:

while True: #outer while
    print("welcome to pythonlife")
    while True: #inner
        print(F"hello everyone")
        print(f"join everyone")
        break
    break

for i in range(10):
    user_name = input("enter username")
    print(user_name)

while True:
    user_name = input("enter username:")
    print(user_name)
    if user_name == "stop":
        break
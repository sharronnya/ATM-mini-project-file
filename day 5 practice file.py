# # # # # # # # syntax:
# # # # # # # #if condition:
# # # # # # # #    statement 1
# # # # # # # #    statement 2
# # # # # # # #    statement n

# # # # # # # age = 19
# # # # # # # if age>=18:# true
# # # # # # #     print(f"you are eligible to vote age is {age}")
# # # # # # #     user_name = input("enter the username:")
# # # # # # #     print(user_name)

# # # # # # # # syntax:
# # # # # # # # if condition:
# # # # # # # #     code block is execute if condition is true
# # # # # # # #else:
# # # # # # # #    code bloack to execute if condition is false

# # # # # # # age = int(input("enter your age:"))
# # # # # # # if age>=18:
# # # # # # #     print(f"you are eligible to vote age is {age}")
# # # # # # # else:
# # # # # # #     print(f"you are not eligible to vote age is {age} under 18")    

# # # # # # user_name = input("enter the username:")
# # # # # # password = input("enter the password:")
# # # # # # if user_name =="arjun" and password == "arjun@123":
# # # # # #     print(F"login success.....")
# # # # # #     print(f"welcome {user_name}")
# # # # # # else:
# # # # # #     print(F"invalid login credentials.....")    

# # # # # #grading system
# # # # # marks = int(input("enter the marks:"))
# # # # # if  marks>=90:
# # # # #     print(f"you gota grade obtained marks {marks}")
# # # # # elif marks>=80:
# # # # #     print(F" you got a b grade obtained marks {marks}")
# # # # # elif marks>=70:
# # # # #     print(F"you got a c grade obatined marks{marks}")
# # # # # elif marks>=60:
# # # # #     print(F"you got a d grade obtained marks {marks}") 
# # # # # elif marks>=35:
# # # # #     print(f"you got pass obtained marks {marks}")
# # # # # # elif marks<=34:
# # # # #     print(f"failed...........") 
    
# # # # marks= int(input("enter the marks:"))
# # # # if marks>100 or marks<0:
# # # #     print(f"please enter marks between 0-100")
# # # # elif marks>=90:
# # # #     print("f you got A grade obtained marks {marks}")

# # # user_name = input("enter the username:")
# # # password = input("enter the password:")
# # # if user_name == "kumar":
# # #     if password =="kumar@123":
# # #         print(F"login succes....")
# # #         print(f"welcome {user_name}")
# # #     else:
# # #         print(F"invalid password .....")    
# # # else:
# # #     print(f"invalid username....")        

# # #) syntax
# # # statement if could else statement
# # # syntax:
# # # result = value_if_true if conditions else value_if_false

# # num_1 =int(input("enter the number:"))
# # result = "even" if num_1%2==0 else "not even"
# # print(result)

# num_1 = int(input("enter the number:"))
# print(f"even") if num_1%2==0 else print(f"not even")
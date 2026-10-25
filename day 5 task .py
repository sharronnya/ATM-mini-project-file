
# # # # # # # # # program to clasiify a number as positive,negative,or zero
# # # # # # # # num = int(input("enter an integer:"))

# # # # # # # # if num > 0:
# # # # # # # #     print("the number is positive.")
# # # # # # # # elif num < 0:
# # # # # # # #     print("the number is nagative.")
# # # # # # # # else:
# # # # # # # #     print("the number is zero.")    

# # # # # # # #2)python program that takes acharacter as input it is a vowel or not
# # # # # # # ch = input("enter the character:")
# # # # # # # if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
# # # # # # #     print("it is a vowel")
# # # # # # # else:
# # # # # # #     print("it is not na vowel")

# # # # # # #3)age gruops of taking persons age as input teenage , adult, old age.
# # # # # # # age of child 0-12 , 12-17, 18-64, 65 older seniour

# # # # # # age = int(input("enter your age:"))
# # # # # # if age >= 0 and age <= 12:
# # # # # #     print("child")
# # # # # # elif age >=13 and age <= 17:
# # # # # #     print("teenage")
# # # # # # elif age >=18 and age <= 64:
# # # # # #     print("adult")
# # # # # # else:
# # # # # #     print("seniour")        

# # # # # #4) program to check weather a leap year or not
# # # # # year = int (input("enter a year:"))
# # # # # if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
# # # # #     print("leap year")
# # # # # else:
# # # # #     print("not a leap year")

# # # # #5) program to calculate final price after applying a 
# # # # # shuold take original price aswell
# # # # price = float(input("enter the orginal price:"))
# # # # discount = float(input("enter the discount percentage:"))
# # # # discount_amount = (price * discount) / 100
# # # # final_price = price - discount_amount
# # # # print("final price:",  final_price)

# # # #6)program to calculate body mass and index (bmi)add height and weight
# # # weight = float(input("enter yuor weight in kg: "))
# # # height = float(input("enter your height in meters:"))
# # # bmi = weight / (height * height)
# # # print("bmi:", bmi)

# # #7)rewriting theb code 
# # x= 8
# # if x % 2 == 0: result = "even"
# # else: result ="odd"
# # #
# # x = 8
# # result = "even" if x % 2 == 0 else "odd"
# # print(result)

# # 8)simple calculator program that takes two numbers 
# # of operators (+,-,*/)
# num1 = float(input("enter first number:"))
# num2 = float(input("enter the second number:"))
# operator = input("enter operator (+,-,*,/):")

# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "/":
#     print(num1 / num2)            
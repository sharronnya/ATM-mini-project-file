# 1) write a python program to covert distance from kilometers to miles
kilometers = float(input("enter distance in kilometers: "))
miles = kilometers * 0.621371
print("distance in miles:", miles)

# write a python program to cocatinate two strings
string_one = input("enter the first string:")
string_two = input("enter the second string:")
result = string_one + string_two
print("concatinated string:", result)

#3) program to calculate simple intrest amount, rate, time in years

amount = float(input ("enter the amount"))
rate = float(input("enter the rate of intrest"))
time = float(input("enter time in years"))
simple_intrest = (amount * rate * time) / 100
print("simple_intrest:",simple_intrest)

#4) program top demonstrate increment to decrement
num = int(input("enter the a number"))
num = num + 1
print("After increment:",num)

num = num - 1
print("After decrement:",num)

#5) calculate the arae of a rectangular lenght, width, area
lenght = float(input("enter lenght:"))
width = float(input("enter width:"))
area = lenght * width
print("Area of rectangle:", area)

#6) program to convert celsius to fahrenheit the formula F = (c*9/5) + 32 take temp in celsius 
celsius = float (input("enter temperature in celsius"))
fahrenheit = (celsius * 9/5) + 32
print ("temperature in fahrenheit:", fahrenheit)
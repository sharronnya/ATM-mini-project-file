#advance functions
#1)square_all(numbers) using map() + lambda
# def square_all(numbers):
    # return list(map(lambda x: x ** 2,numbers))
# numbers = [1,2,3,4,5]
# print(square_all(numbers))

#2)filter_positive(numbers)using filter +lambda
# def filter_positive(numbers):
    # return list(filter(lambda x: x > 0,numbers))
# numbers = [-4,-3,0,5,8,-1,7]

# print(filter_positive(numbers))

#3)calculate_factorial(n)using reduce()+lambda
# from functools import reduce
# def calculate_factorial(n):
    # return reduce(lambda x,y: x * y,range(1, n + 1))
# print(calculate_factorial(6)) #x = previous result  #y = next value in the list

#4)count_vowels(string) using reduce() + lambda
# from functools import reduce
# def count_vowels(string):   #string anedi 0 tho start avtadi andukea 0 petam
    # return reduce(lambda count,char:count + (1 if char.lower() in "aeiou" else 0), string,0 )
# print(count_vowels("welcome to pythonlife"))
#if char lower capital una words ni small ga marchi check easy ga chestundi
#else 0 enduku petam antea 0 tho start avtadi char untea 1 add avtadi ledantea 0 chupisthadi (ie else) lo
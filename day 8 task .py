#reverse list 
# write a python code to reverse the olderof elementsin the given list#my list
# print the riversed list my_list=[10,20,30,40,50,11]
# my_list = [10,20,30,40,50,11]
# reversed_list = my_list[::-1]
# print(reversed_list)

#2)common elements
# given two list list1 and list 2 find and print the common elementys between
#list1 =[1,2,3,4,5]
#list2 = [4,5,6,7,8]

# list1 = [1,2,3,4,5]
# list2 = [4,5,6,7,8]
# for i in list1:
    # if i in list2:
        # print(i)

#3)create a new list unique list containing only the unique elements from the given list
#original list. print the unque list
# originnal_list = [1,2,3,4,4,5]

# original_list = [1,2,3,4,4,5]
# unique_list = []
# for i in original_list:
    # if i not in unique_list:
        # unique_list.append(i)

# print(unique_list)        

#4)write a python script that concatinate two list and print the result
# list1 = ["laxmi"]
# list2 = ["saranya"]
# result = list1+list2
# print(result)

#5)write a python script that repeats a list three times and prints the results
#numbers= [1,2,3,7,1,3,0,2,1,5]
# numbers = [1,2,3,7,1,3,0,2,1,5]
# result = numbers * 3
# print(result)

#6)write a python script that removes the elements at even indices from a list
# 0,2,4 even elements
# fruits = ["apple","banana","mango","orange","grapes","kiwi"]
# result = fruits[1::2]
# print(result)

#7)remove duplicate elements from the given list
#withuot duplicates while preserving the order
#duplicated_list and print the list
#duplicated_list= [1,2,2,3,4,4,5]

# duplicated_list = [1,2,2,3,4,4,5]
# new_list = []
# for i in duplicated_list:
    # if i not in new_list:
        # new_list.append(i)
# print(new_list)   


#9)list comprehensions
#square numbers create a list of squares of numbers from 1 to 10.
# squares = [i ** 2 for i  in range(1,11)]
# print(squares)

#10)list insertion  write a python script that inserts the numbers 10, 11, and 12 at the begining of a list
# numbers = [1,2,3,4,5]
# numbers = [10,11,12] + numbers
# print(numbers)

#11)even numbers generate a list of even numbers from 1 to 20.
# empty_list = []
# for i in range(1,21):
    # if i%2==0:
        # empty_list.append(i)
# print(empty_list)        

#12)words lenght given a list of words  create list containing the lenghts of each word
# words = ["apple", "banana", "cherry","dates"]
# words = ["apple", "banana", "cherry","dates"]
# lenghts = [len(words) for words in words]
# print(lenghts)
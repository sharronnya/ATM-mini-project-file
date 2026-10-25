#list methods
#append
# numbers = [3,1,4,1,5,9,2,6,5]
#syntax
# var.methodname(arguments) #within the paranthesis
# numbers.append("pythonlife")
# print(numbers)

# numbers.append([1,2,3,4,])
# print(numbers)

#extend
# numbers = [3,1,4,1,5,9,2,6,5]
# numbers.extend(["pythonlife","kiran","vasu","srikanth","joseph"])
# print(numbers)

#copy
# numbers = [3,1,4,1,5,9,2,6,5]
# sample = numbers.copy()
# print(sample)
# sample.append("pythonlife")
# print(sample)

# print(f"original list {numbers}")


# clear
# numbers = [3,1,4,1,5,9,2,6,5]
# numbers.clear()
# print(numbers)

#count
# numbers = [3,1,4,1,5,9,2,6,5,1,1,1,1,1,1,1,1,1,1]
# print(numbers.count("pythonlife"))

# numbers = [3,1,4,5,9,2,6,5,1,1,1,1,1,1,1,1,1,1,1]
# print(numbers.count(1))

#index    #returns the index of the first occurance of a 
 #specified item in the list.

# numbers = [3,1,4,5,9,2.6,5,1,1,1,1,1,1,1,1,1,1,1]
# print(numbers.index(5))

#numbers.remove(1)   #removing the first occurance of 1
# numbers = [3,1,4,1,5,9,2,6,5,1,1,1,1,1,1,1,1,1,1,1,]
# numbers.remove(1)
# print(numbers)

# list_1 = [20,30,40,50]
# list_1.remove(30)
# print(list_1)

#pop
# numbers=[3,1,4,1,5,9,2,6,5,1,1,1,1,1,1,1,1,]
# numbers.pop(0)
# print(numbers)


# numbers = [3,1,4,1,5,9,2,6,5,1,1,1,1,1,1,1,1,]
# obj = numbers.pop(6)
# print(numbers)


# print(obj)  

#insert
# numbers = [3,1,4,1,5,9,2,6,5,1,1,1,1,1,1,1,1,1]
# numbers.insert(10,"pythonlife")

#reverse
# numbers = [3,1,4,1,5,9,2,6,5,1,1,1,1,1,1,1,1,1,]
# numbers.reverse()
# print(numbers)

# numbers.sort() # sorting the list
# numbers = [3,1,4,1,5,9,2,6,5]
# numbers.sort(reverse=True)
# print(numbers)

#expression for item in iterable
# empty_list = []
# for i in range(1,11):
    # result = i**2
    # empty_list.append(result)
# print(empty_list)

# result = [i**2 for i in range(1,11)]
# print(result)


# empty_list = []
# for i in range(1,11):
    # if i%2==0:
        # empty_list.append(i)

#expression for item in seq if cond
# result = [i for i in range(1,11) if i%2==0]
# print(result)


# numbers = [3,1,4,1,5,9,2,6,5,1,1,1,1,1,1,1,1,1,]
# for i in numbers:
    # if i == 1:
        # numbers.remove(i)
# print(numbers)

#  to permanantly remove 1 from this list we use this method
numbers = [3,1,4,1,5,9,2,6,5,1,1,1,1,1,1,1,1,1,1,1,1]
empty_list = []
for i in numbers:
    if i!=1:
        empty_list.append(i)

print(empty_list)

#conscise way

result = [i for i in numbers if i!=1]
print(result)
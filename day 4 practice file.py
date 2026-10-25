# arithmetic operators 
# operator contains symbol or keyword
# operand contains value or variable
# (+)
num_1 = 10
num_2 = 10
result = num_1 + num_2
print(result)

# strings always concatinate
num_1 = "python" 
num_2 = "life"
result = num_1 + num_2
print (result)

# (-)
num_1 = 10
num_2 = 5
result = num_1 - num_2
print (result)
# subracts  the right operand from left operand
num_1 = 10
num_2 = 5                     
result = num_2 - num_1
print(result)

# (*)
num_1 = 10
num_2 = 5
result = num_1 * num_2
print(result)

#/divison always returns qoeiasnt divides the left operand by the right  operand
num_1 = 10
num_2 = 5
result = num_1 / num_2
print(result)

# // floar divison it provides only integer part removes decimal part
num_1 = 10
num_2 = 5
result = num_1 // num_2
print (result)

# % module s it gives reminder 
num_1 = 10
num_2 = 3
result = num_1 % num_2
print(result)

# ** exponentition lest operand always base value right operand always exponent power
num_1 = 4
num_2 = 2
result = num_1 ** num_2
print(result)

#2) assighnment operators contains +=, -=, *=,
rice = 999
rice += 1
print(rice)
#eq-->
num_1 = 100
num_1 -= 1
print(num_1)

#3) comparison operators it used to contain values and try to return boolean of (true) or (false)
product_cost = 1000
product_cost_2 = 1000
print(product_cost==product_cost_2)

product_cost = 999
product_cost_2 = 1000
print(product_cost != product_cost_2)

product_cost = 999
product_cost_2 = 1000
print(product_cost < product_cost_2)

product_cost = 1000
product_cost_2 = 1000
print(product_cost < product_cost_2)

product_cost = 1000
product_cost_2 = 1000
print(product_cost <= product_cost_2)

product_cost = 1000
product_cost_2 = 999
print(product_cost > product_cost_2)

product_cost = 1000
product_cost_2 = 1000
print(product_cost >= product_cost_2)

product_cost = 1000
product_cost_2 = 1000
print(product_cost > product_cost_2)

# logical operator and, or, not, used to combine multiple conditions
#and condition every condition shuould be true
user_name ="arjun"
password = "arjun@123"
print(user_name == "arjun" and password == "arjun@123")

# one condition is enough to show true it represents true ,
# every comndition shuold be false then it represents false
user_name = "arjun"
password = "arjun@123"
print(user_name == "arjun" or password == "arjun@12345")

# not if it shows (false) it returns (true) it it shows (true) it returns (false)
sample = True
print(not sample)

sample_2 = False
print(not sample_2)

#5) identity operators to findout memory address
# is true
# is not true
# it checks same varaiables or there or not
sample = [1,2,2,4]
print(sample)
a = sample
print(id(sample))
sample_2 = [1,2,3,4,5]
b = sample_2
print(id(sample_2))

# -5 to 256 are stored in cache is about guaranteed integer caching imp
# is (true)
a= 256
b= 256
print(a is b)

# some long digits also storing in same memory addressb in python so its returning (true)
#is not (true)
a = 23456677878
b = 23456677878
print(a is b)

# membership data types 
#operatoprs are used to test weather values or there in sequence or not
# example ,list,tuple, string.
#(in) returns true if value is found in sequence
#(not in) returns true if value is not found in sequence
# list, tuples, strings, are ordered sequence

voter_data  = ["vasu","saranya","sai", "prameela"]
print ("vasu" in voter_data)
print ("kiran" not in voter_data)

fruits = ["oranges","bananas","apples"]
print ("apples" in fruits)
print ("kiwi"not in fruits)

sentence = "welcome to python life"
print("to"in sentence)
print("0r"in sentence)

# discount 
product_cost =10000
discount =10
result = product_cost * (discount/100)
print(result)
print(product_cost-result)
print(product_cost)
product_cost -=result #eq-->pc pc - r
print(product_cost)


product_cost = 10000
discount = 10
result = product_cost * (discount/100)
product_cost -= result


# output formating(f)strings
#**
num_1 = 5 
num_2 = 2
result = num_2 ** num_1
print(result)
print(f"base value {num_2} and powerof {num_1} and result is {num_2**num_1}")
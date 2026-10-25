#create strings
# single_quoted_string = 'hello world!'
# print(single_quoted_string)
# print(type(single_quoted_string))

# duble_quoted_string = "python strings"
# print(duble_quoted_string)
# print(type(duble_quoted_string))

# triple_quoted_string = '''triple quotes allow
# strings to span multiple lines.'''
# print(triple_quoted_string)
# print(type(triple_quoted_string))

# sample = ""
# print(sample)
# print(type(sample))

# sample_2 = str()
# print(sample_2)
# print(type(sample_2))

# my_string = "python life"
# print(len(my_string))

#syntax
#var[index value]
# my_string = "python life"
# print(my_string[2])
# print(my_string[-2])


#positive indexing forward direction
# p y t h o n l i f e
#syntax 
# seq[s:s:s]
# sample = "python life"
# print(sample[2:5])

# sample = "python life"
# print(sample[7:11])

# forward direction negative indexing -1 -2 -3 -4 -5 -6 -7 -8 -9
# sample = "python life"
# print(sample[-4:])

# sample = "python life"
# print(sample[-9:-6])                            space kuda oka character ah

#backward direction lo nagative index starts from -1 -2 -3 -4 -5 -6 -7 -8 -9
# -1 step value lo pedte characters ani return avtai
# sample = "python life"
# print(sample[-2:-5:-1])

#backard direction positive indexing 0 1 2 3 4 5 6 7 8 9 
# sample = "python life"
# print(sample[9:6:-1])

# string methods
#upper
#lower
# message = "Hello , world!"
# sample = message.upper()
# print(sample)

# print(message)

#lower
# message =  "HELLO , World!"
# sample = message.lower()
# print(sample)

#count
# sentence = "This is a sample sentence."
# count_i = sentence.count('sample')

# print(count_i)

# strip right side left side 
# right side isthea strip alanea untadhi
# left side isthea strip alanea untadi
# whitespace_string = "  this is a string with leading and trailing whitespace.  "
# stripped_string = whitespace_string.lstrip()

# print(stripped_string)

# lenght
# my_string = "python is fun and powerful"
# lenght_of_string = len(my_string)

# print(lenght_of_string)

#split imp topic 
# data = "pythonlife, kiran,123456"
# data1 = data.split(',')

# print(data1)

#replace
# original_string =  "python is fun!"
# modified_string = original_string.replace('fun' , 'awesome')

# print(modified_string)

#starts with
#ends with

# filename = "example.txt"
# starts_with = filename.startswith("ex")
# ends_with = filename.endswith(".txt")

# print(starts_with)
# print(ends_with)

# find and index
# sentence = "this is a sentence."
# position_a = sentence.find('a')
# position_1 = sentence.index('a')

# print(position_a)
# print(position_1)

#capitalize
# text = "python programing"
# capitalized_text = text.capitalize()

# print(capitalized_text)


# is_alpha # is_numeric
# numeric_string = "12345"
# alphap_string = "python"

# is_numeric = numeric_string.isdigit()
# is_alpha = alphap_string.isalpha()

# print(is_numeric)
# print(is_alpha)

# join 
# world_list = ['Hello','World']
# joined_string = ' '.join(world_list)

# print(joined_string)
#python list

# list_1 = []   # -->empty list
# print(list_1)
# print(type(list_1))


#different data types including nested list
# list_2 = [1,5.7,True,"pythonlife",[1,2,3],(1,2,3),{1,2,3},]
# print(type(list_2))

# list_3 = list()
# print(list_3)
# print(type(list_3))

# my_list = [10,20,30,40,50]
# print(len(my_list))


#positive indexing
# my_list = [10,20,30,40,50] # positive values,0,1,2,3,4,5 
#syntax
#seq[indexvalue]
# print(my_list[2])#30
# print(my_list[4])#50
# print(my_list[0])#10

#negative indexing
# my_list = [10,20,30,40,50] # negative values backword direction -1,-2,-3,-4,-5
# print(my_list[-3])#30
# print(my_list[-1])#50
# print(my_list[-5])#10

# slicing 
#forward direction positive index slicing 
my_list = [10,20,30,40,50,60,70,80] #-->0,1,2,3,4,5,6,7,8,
#seq[s:s:s]-->start,stop,step
print(my_list[0:8:2])
#start value = 0 teskuntadi
#stop value = end teskuntadi
#step value = 1 em ichina ivakapoyina 1 teskuntadi
print(my_list[2:5])
print(my_list[:3])
print(my_list[5:8])
print(my_list[3:6])

#forward direction negative indexing
my_list = [10,20,30,40,50,60,70,80]  #-->-1 ,-2,-3,-4,-5,-6,-7,-8,-9
print(my_list[-4:-1])#50,60,70
print(my_list[-8:-5])#10,20,30
print(my_list[-4:-2])#50,60
print(my_list[-2])#70, 80

#backword direction positive indexing  (step value -1 peteyali)
my_list = [10,20,30,40,50,60,70,80] #-->0,1,2,3,4,5,6,7
print(my_list[7:4:-1])#80,70,60
print(my_list[2:1:-1])#30,20,10
print(my_list[4:2:-1])#50,40

#backward direction negative indexing
my_list = [10.20,30,40,50,60,70,80] #-->-1,-2,-3,-4,-5,-6,-7,-8
print(my_list[-1:-4:-1])#80,70,60
print(my_list[-6:-1])#30,20,10
print(my_list[-4:-6:-1])#50,40

#slicing
matrix = [[1,2,3] [4,5,6] , [7,8,9]]
#print(len(matrix))
print(matrix[1][2])
print(matrix[0][2])
print(matrix[2][0])
# import array as arr
from array import *

val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

for i in range(0, len(val)):
    print(val[i] , end=" ")


print('\n')

# for x in val:
#     print(x, end=",")

# print('\n')

# print(val.typecode)

# val.reverse()
# for i in range(0, len(val)):
#         print(val[i] , end=" ")

# print('\n')

# val.insert(1, 30)
# val.append(40)
# val[2] = 50

# copyArray = array(val.typecode, (x*3 for x in val))

# copyArray.pop(3)
# copyArray.remove(24)

#using slicing
#a = val[start idx : end idx]
#a = val[2:5]
#a = val[2:-1]
#a = val[::-1]


#user input array

# arr = array('i', [5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

# n = int(input("Enter the number: "))

# for i in range(0, n):
#     arr.append(int(input('enter next input:')))

# for x in arr:
#     print(x, end=" ")

#searchin for element in an array

arr = array('i', [6, 12, 18, 24, 30, 36, 42, 48, 54, 60])

i = arr.index(24)

print(i)
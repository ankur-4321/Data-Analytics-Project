# import numpy as np
# arr = np.array([1,5,6,8])
# print(arr)

# import numpy as np
# arr = np.array([[1,4,6,9],[5,4,8,9]])
# print(arr[0,1])

# import numpy as np
# arr = np.array([[[2,3,5],[6,9,5]],[[6,8,3],[8,9,6]]])
# print(arr)


# Use this array for all questions: 
# arr = np.array([[10,20,30],[40,50,60],[70,80,90]]) 

# Q1. Print the complete array.
# import numpy as np

# arr = np.array([[10,20,30],
#                 [40,50,60],
#                 [70,80,90]])
# print(arr)

# print(arr.ndim)

# print(arr.shape)

# print(arr[0,0])

# print(arr[1,1])

# print(arr[2,2])

# print(arr[0])

# print(arr[1])

# print(arr[:,0])

# print(arr[:,1])

# print(arr[2,1])

# print(arr[-1])

# print(arr[:,-1])

# print(arr[1,1])

# print(arr[1,0])
# print(arr[1])
# print(arr[0])

import numpy as np
# arr = np.array(['a','n','k','u','r'])
# print(arr.dtype)

# arr = np.array([1.0,7.9,6.8,7.8])
# new_arr = arr.astype('int')
# print(new_arr)
# print(new_arr.dtype)

# arr = np.array([1,2,3,4,5])
# new_arr = arr.view()
# new_arr[0] = 11
# print(new_arr)
# print(arr)

# n = np.array([3,4,5,6,7,8,9,10])
# new_arr = n.reshape(2,4)
# print(new_arr)

# n = np.array([[4,5,6,7],[8,9,10,11]])
# x = n.reshape(8)
# print(x)

# n = np.array([2,3,4,5,7,8,9,10,3,7,8,9])
# x = n.reshape(2,2,3)
# print(x)

# # Q1 Create a 3x3 array and print the first row using slicing.
# arr = np.array([[10, 20, 30],
#                  [40, 50, 60],
#                  [70, 80, 90]])
# print(arr[0, :])

# Q2 Print the last row using slicing.
# print(arr[-1, :])

#  Q3 Print the first column using slicing.
# print(arr[:, 0:1])

# Q4 Print the second column using slicing
# print(arr[:, 1:2])

#  Q5 Print the last column using slicing.
# print(arr[:, 2:3])

# Q6 Print the first two rows.
# print(arr[:2, :])

#  Q7 Print the last two rows.
# print(arr[1:, :])

# Q8 Print the first two columns.
# print(arr[:, :2])

# Q9 Print the last two columns.
# print(arr[:, 1:])

# Q10 Print the sub-array [[20,30],[50,60]]
# print(arr[:2, 1:])

# Q11 Print the sub-array [[40,50],[70,80]].
# print(arr[1:, :2])

# Q12 Print only the middle row of a 3x3 array.
# print(arr[1:2, :])

# Q13 Print only the middle column of a 3x3 array.
# print(arr[:, 1:2])

# Q14 Print all elements except the first row
# print(arr[1:, :])

# Q15 Print all elements except the last row
# print(arr[:-1, :])

# Q16 Print all elements except the first column.
# print(arr[:, 1:])

# Q17 Print all elements except the last column.
# print(arr[:, :-1])

# Q18 Print the complete array using slicing only.
# print(arr[:, :])

# Q19 Using arr = np.array([10,20,30,40,50,60]), print every second element using slicing.
# print(arr[::2])

# Q20 Using arr = np.array([10,20,30,40,50,60]), print elements from index 1 to 4 using slicing.
# print(arr[1:5])

# n = np.array([1,2,3,5,7])
# x = np.array([3,5,8,9,5])
# v = np.concatenate((n,x))
# print(v)

# n = np.array([[1,2,3],[5,7,9]])
# x = np.array([[3,5,8],[9,5,8]])
# v = np.concatenate((n,x), axis=1)
# print(v)

# n = np.array([[2,8,7,6],[5,6,2,5]])
# arr_n = np.array_split(n,2, axis=1)
# print(arr_n) 

# n = np.array([3,4,6,7,8,9,10])
# v = np.where(n==10)
# print(v)

# n = np.array([4,8,9,3,5,2,5])
# v = np.where(n>2)
# print(v)

# from numpy import random
# v = random.randint(100,size=(3,5))
# print(v)

# v = random.rand(2,3)
# print(v)

# y = random.choice([5,6,8,9], size=(2,3))
# print(y)

# marks = []

# # Q1 Concatenate arrays a=[10,20,30] and b=[40,50,60]
# a = np.array([10,20,30])
# b = np.array([40,50,60])

# X = np.concatenate((a,b))
# print(X)

# # Q2 Join two 2x2 arrays row-wise (axis=0)
# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])

# print(np.concatenate((a,b), axis=0))

# # Q3 Join two 2x2 arrays column-wise (axis=1)
# print(np.concatenate((a,b), axis=1))

# # Q4 Use hstack() to join two 1D arrays.
# a = np.array([1,2,3])
# b = np.array([4,5,6])

# print(np.hstack((a,b)))

# # Q5 Use vstack() to join two 1D arrays.
# print(np.vstack((a,b)))

# # Q6 Split [10,20,30,40,50,60] into 3 equal parts.
# arr = np.array([10,20,30,40,50,60])

# print(np.split(arr,3))

# # Q7 Split [1,2,3,4,5,6,7,8] into 4 equal parts.
# arr = np.array([1,2,3,4,5,6,7,8])

# print(np.split(arr,4))

# # Q8 Split a 4x2 array into 2 arrays row-wise.
# arr = np.array([[1,2],[3,4],[5,6],[7,8]])

# print(np.array_split(arr,2,axis=0))

# # Q9 Split a 2x4 array into 2 arrays column-wise.
# arr = np.array([[1,2,3,4],[5,6,7,8]])

# print(np.array_split(arr,2,axis=1))

# # Q10 Use array_split() to split [1,2,3,4,5,6,7] into 3 parts.
# arr = np.array([1,2,3,4,5,6,7])

# print(np.array_split(arr,3))

# # Q11 Find index of 40 in [10,20,30,40,50].
# arr = np.array([10,20,30,40,50])

# print(np.where(arr==40)[0])

# # Q12 Find all indices of 5 in [1,5,3,5,7,5].
# arr = np.array([1,5,3,5,7,5])

# print(np.where(arr==5)[0])

# # Q13 Find all even numbers from [11,12,13,14,15,16].
# arr = np.array([11,12,13,14,15,16])

# print(arr[arr%2==0])

# Q14 . Find values greater than 50 from [25,60,45,80,90].
X = np.array([25,60,45,80,90])

print([X>50])

# Q15 Find positions where 100 occurs in [50,100,20,100,70].
arr = np.array([50,100,20,100,70])

print(np.where(arr==100)[0])

# Q16 Sort [50,20,10,40,30].
arr = np.array([50,20,10,40,30])

print(np.sort(arr))

# Q17 Sort [99,15,75,25,50].
arr = np.array([99,15,75,25,50])

print(np.sort(arr))

# Q18 Sort ['banana','apple','mango','orange'] alphabetically
arr = np.array(['banana','apple','mango','orange'])

print(np.sort(arr))

# Q19 Sort rows of [[3,2,1],[6,5,4]].
arr = np.array([[3,2,1],[6,5,4]])

print(np.sort(arr))

# Q20 Sort [10,40,20,60,30] and print largest value.
arr = np.array([10,40,20,60,30])

sorted_arr = np.sort(arr)
print(sorted_arr)
print("Largest:", sorted_arr[-1])

# Q21 Concatenate three arrays into one array.
a = np.array([1,2])
b = np.array([3,4])
c = np.array([5,6])

print(np.concatenate((a,b,c)))

# Q22 Split an array of 12 elements into 6 equal parts.
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print(np.split(arr,6))

# Q23 Find all indices where value 25 occurs.
arr = np.array([25,10,25,30,25])

print(np.where(arr==25)[0])

# Q24 Sort an array in descending order.
arr = np.array([50,20,10,40,30])

print(np.sort(arr)[::-1])

# Q25 Search all numbers divisible by 3 from [3,5,6,8,9,12,15].
arr = np.array([3,5,6,8,9,12,15])

print(arr[arr%3==0])
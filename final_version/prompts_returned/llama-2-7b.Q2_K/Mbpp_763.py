"""
Write a python function to find the minimum difference between any two elements in a given array. 
assert find_min_diff((1,5,3,19,18,25),6) == 1
"""
import math
def find_min_diff(array):
    min = -1     #initializing the minimum value to-1
    for (i, j) in enumerate(enumerate(array)):
        if i != j:   #checking that i and j are not same element
            print(i,j,len(array))#printing the elements of array
            min = min if math.fabs(i - j) < min else i - j
    return (min + 1)
a=[200,5,34,12,90]
b=find_min_diff(a)
print("the minimum difference between any two elements in a given array is: ",b)
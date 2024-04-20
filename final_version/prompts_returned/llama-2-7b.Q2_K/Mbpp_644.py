"""
Write a python function to reverse an array upto a given position.
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
"""
import math
def reverse_Array_Upto_K(arr, index): #return an array of length arr.lenght-index plus one, such that the first item is the last element in original array.
    temp = []
    for i in range(0,len(arr)):
        if len(temp)==index+1:
            break
        else:
            temp.append(arr[i])
            
    
    return reverse_Array_Upto_K(temp, index - 1) + [arr[-1]]
        
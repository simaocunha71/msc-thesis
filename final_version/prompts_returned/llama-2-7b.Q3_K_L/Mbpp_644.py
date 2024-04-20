"""
Write a python function to reverse an array upto a given position.
assert reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4) == [4, 3, 2, 1, 5, 6]
"""

def reverse_Array_Upto_K(array,k):
    j=0
    for i in range(0,len(array)):
        #print (i,j)
        if j==k:
            break
        array[i],array[j]=array[j],array[i]
        j+=1
    
        
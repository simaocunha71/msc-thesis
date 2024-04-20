"""
Write a python function to find the sum of all odd length subarrays. 
assert odd_length_sum([1,2,4]) == 14
"""
from typing import Optional
def odd_length_sum(arr: [int]) -> int: 
    if len(arr) < 3: # base case for the empty array.
        return 0;
    
    # create a temporary list and add all elements of the input array to it.
    l = []
    i=1
    j=2
    while True:
        if arr[i] == None:
            break;
        else:
            l.append(arr[i])   # adding element to temporary list 
            i+=1 # incrementing index by one for the current element in input array.
            
    # base case for the empty subarray of length 0.
    if len(l) == 0:
        return 0;
    
    sum = 0                     
    j=3 # base case for odd length subarrays

    while j < len(arr):
        s1 = l[-1]             # get the last element in temporary list.        
        if int(s1) % 2 == 1:   # checking condition of the current element (temp list).
            sum = sum + int(s1);     
            del l[-1];              
    return sum;
arr= [int(x) for x in input('Enter array ')]          
print(odds_sum(arr))
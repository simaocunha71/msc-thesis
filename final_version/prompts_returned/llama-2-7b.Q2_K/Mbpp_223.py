"""
Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
"""
import math

def is_majority(array, length, item):
    "Check if the given array has a majority element."
    index = math.ceil(length/2.0)
    majority = False
    
    for i in range(index+1, index-1, -1):
        if array[i] == item:
            return True
    for i in range(index-1, index-1,-1):
        if array[i] == item:
            majority = True
    
    return majority
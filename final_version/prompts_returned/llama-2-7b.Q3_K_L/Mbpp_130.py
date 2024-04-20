"""
Write a function to find the item with maximum frequency in a given list.
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
"""

def maxOccur(arr):
    count = [0]*len(arr)
    for i in arr:
        if count[i] == 0 or count[i]+1 > max_count:
            max_count = count[i]+1
            max_value = i
    return max_value, max_count
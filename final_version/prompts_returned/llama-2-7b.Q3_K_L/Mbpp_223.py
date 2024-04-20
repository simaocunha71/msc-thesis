"""
Write a function that takes in a sorted array, its length (n), and an element and returns whether the element is the majority element in the given sorted array. (The majority element is the element that occurs more than n/2 times.)
assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
"""
# @Coded by - Akash Kumar Singh ( akash7469@gmail.com )
import collections
def isMajority(A, n, item):
    if len(A) < n:
        return False
    
    count = collections.Counter()
    for ele in A:
        count[ele] += 1
    most_common_item = max(count, key=count.get)
    return (most_common_item == item)
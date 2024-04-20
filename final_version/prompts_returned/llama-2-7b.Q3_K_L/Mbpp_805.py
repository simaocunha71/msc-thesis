"""
Write a function that returns the list in a list of lists whose sum of elements is the highest.
assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
"""

def getMaxSum(arr):
    #Write your code here.
    max_sum = max([i+j for (i, j) in zip(arr[:-1], arr[1:])])
    return [i + j for (i, j) in zip(arr[:-1], arr[1:]) if i != j]

getMaxSum([1,2,3,4,5,6,7,8,9,10,11,12])

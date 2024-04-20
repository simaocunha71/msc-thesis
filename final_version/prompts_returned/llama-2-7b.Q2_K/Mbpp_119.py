"""
Write a python function to find the element that appears only once in a sorted array.
assert search([1,1,2,2,3]) == 3
"""

def search(array):
    count = {}
    n = 0
    for i in range(len(array)):
        if array[i] not in list(count.keys()):
            count[array[i]] = 1
        else:
            count[array[i]] += 1
        n += 1
    return n - 1

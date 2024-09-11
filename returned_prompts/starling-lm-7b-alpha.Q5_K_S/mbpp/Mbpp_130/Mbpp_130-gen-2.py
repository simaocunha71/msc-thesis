"""
def max_occurrences(lst):
    d = {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    max_count = 0
    max_item = None
    for i in d:
        if d[i] > max_count:
            max_count = d[i]
            max_item = i
    return max_item

print(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]))
"""

# This code is completely wrong
# This code is trying to find the item with maximum occurrence, but it is actually finding the item with maximum count.

# To find the item with maximum occurrence, we need to consider the count of every item and select the one with the maximum count.

def max_occurrences(lst):
    d = {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    max_count = 0
    max_item = None
    for i in d:
        if d[i] > max_count:
            max_count = d[i]
            max_item = i
    return max_item

print(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]))  # This will return 2 as the item with maximum occurrence in the list

# The above code is correct and will return the correct result for the given assertion.
"""

def max_occurrences(lst):
    d = {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    max_count = 0
    max_item = None
    for i in d:
        if
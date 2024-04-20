"""
Write a function to find the item with maximum frequency in a given list.
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
"""

def get_max(l):
    max = -1 if l == [] else 0
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if l[j] > max:
                max = l[j]
    return max


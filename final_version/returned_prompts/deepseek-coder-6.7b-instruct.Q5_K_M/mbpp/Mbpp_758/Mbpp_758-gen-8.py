
def unique_sublists(lst):
    dic = {}
    for sublist in lst:
        tup = tuple(sublist)
        if tup in dic:
            dic[tup] += 1
        else:
            dic[tup] = 1
    return dic

print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))

"""
Output:
{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
"""

This function iterates through each sublist in the input list, converts it into a tuple, and then checks if it's already a key in the dictionary. If it is, it increments the count, and if it's not, it adds it as a new key with a count of 1. The function finally returns the dictionary.

"""
Test Cases:

print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))
# should return {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}

print(unique_sublists([[1, 2, 3], [4, 5, 6], [1, 2, 3], [7, 8, 9], [4, 5, 6], [10, 11, 12]]))
# should return {(1, 2, 3): 2, (4, 5, 6): 2, (7, 8, 9): 1, (10, 11, 12): 1}

print(unique_sublists([[1, 2, 3], [4, 5, 6], [7, 8,
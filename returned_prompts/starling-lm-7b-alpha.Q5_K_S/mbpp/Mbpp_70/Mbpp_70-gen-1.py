"""
def get_equal(list_of_tuples):
    if len(list_of_tuples) == 0:
        return True
    length = 0
    for i in list_of_tuples:
        if len(i) != 0:
            length = len(i)
            break
    else:
        return False
    for i in list_of_tuples:
        if len(i) != length:
            return False
    return True
"""
def get_equal(list_of_tuples):
    if len(list_of_tuples) == 0:
        return True
    length = len(list_of_tuples[0])
    for i in list_of_tuples:
        if len(i) != length:
            return False
    return True

# Testing
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
assert get_equal([(11, 22), (33, 44, 55)]) == False

"""
Explanation:

First, we check if the list of tuples is empty. If it is, then all the tuples have the same length (since there are no tuples to compare).

Otherwise, we get the length of the first tuple in the list. If the first tuple is empty, then no tuple in the list can have the same length as any other tuple.

Finally, we check if all the tuples have the same length as the first tuple. If they don't, then the function returns False.
"""

# Time Complexity: O(n), where n is the number of tuples in the list.
# Space Complexity: O(1), because we don't use any extra space that scales with the size of the input.

# Python3 program to check if two strings are anagram of each other

# Function to check if two strings are anagram of each other
def areAnagram(a, b):
    # Remove white spaces and convert both strings to lowercase
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()
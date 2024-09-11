"""
def rear_extract(tuples_list):
    return [t[2] for t in tuples_list]
"""

# Alternate Solution:
def rear_extract(tuples_list):
    return [t[2] for t in tuples_list if len(t) > 2]



# Test
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
# assert rear_extract([(1, 'Rash'), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [None, 20, 19]
# assert rear_extract([(1, 'Rash'), (2, 'Varsha'), (3, 'Kil')]) == [None, None, None]
# assert rear_extract([]) == []
# assert rear_extract([(1, 'Rash', 21)]) == [21]


# Python3 Version:
# def rear_extract(tuples_list):
#     return [t[2] for t in tuples_list if len(t) > 2]

# Python2 Version:
# def rear_extract(tuples_list):
#     return [t[2] for t in tuples_list if len(t) >= 2]


# Time Complexity: O(n), n is the length of tuples_list
# Space Complexity: O(1)


# Python3
# def rear_extract(tuples_list):
#     return [t[2] for t in tuples_list if len(t) > 2]

# Python2
# def rear_extract(tuples_list):
#     return [t[2] for t in tuples_list if len(t) >= 2]


# Time Complexity: O(n), n is the length of tuples_list
# Space Complexity: O(1)


"""
In the above function, we use list comprehension to iterate through the list of tuples and
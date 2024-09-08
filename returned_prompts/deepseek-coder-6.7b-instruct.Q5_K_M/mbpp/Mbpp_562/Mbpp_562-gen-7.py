
def Find_Max_Length(lst):
    max_len = max(len(sublist) for sublist in lst)
    return max_len

print(Find_Max_Length([[1],[1,4],[5,6,7,8]]))

"""
Output:
4
"""

Explanation:

The function Find_Max_Length takes a list of sublists as an input. It uses the built-in max function with a generator expression to find the maximum length of a sublist. The generator expression iterates over each sublist in the input list and calculates its length, returning the maximum of these lengths. This is the length of the longest sublist.

The function then returns this maximum length.

For the input [[1],[1,4],[5,6,7,8]], the maximum length of a sublist is 4 (the third sublist [5,6,7,8]). So, the function returns 4.
"""

# Task 3


def neg_nos(lst):
    return [i for i in lst if i < 0]

# Test
print(neg_nos([-1,4,5,-6])) # [-1, -6]





"""

"""


# Original code:

# This code creates a new list called 'neg_nos' using a list comprehension to filter out the negative numbers from a given list 'lst'. The condition `i < 0` is used to select only the negative numbers. The function `neg_nos` is then tested with the input `[-1,4,5,-6]` and the expected output `[-1,-6]` is printed.

# The function `neg_nos` takes a single argument `lst`, which is the input list of numbers. It uses a list comprehension to iterate over each element `i` in the input list. The condition `i < 0` is used to filter out only the negative numbers from the list. The resulting list of negative numbers is returned by the function.

# The test case `print(neg_nos([-1,4,5,-6]))` is used to verify the correctness of the function. It calls the `neg_nos` function with the input `[-1,4,5,-6]` and prints the resulting list `[-1,-6]`. This indicates that the function is correctly returning the negative numbers from the input list.


# Here are some more test cases to further validate the function:

# print(neg_nos([1, -2, 3, -4])) # [-2, -4]
# print(neg_nos([5, -6, 7, -8])) # [-6, -8]
# print(neg_nos([])) # []
# print(neg_nos([0])) # []
# print(neg_nos([-1])) # [-1]

# These test cases cover different scenarios, including an empty list, a list with no negative numbers, a list with only negative numbers, and a list with both positive and negative numbers. The function correctly returns the negative numbers for all these cases.

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""
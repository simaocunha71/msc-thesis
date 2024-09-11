"""
Here is a function that can subtract two lists element-wise:

def sub_list(list1, list2):
    return [a-b for a, b in zip(list1, list2)]
"""

def sub_list(list1, list2):
    return [a-b for a, b in zip(list1, list2)]

assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]







"""
Here is how it works:

The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc. When iterating over the zip object, it yields the pairs.
For example, zip([1, 2, 3], [4, 5, 6]) would return [(1, 4), (2, 5), (3, 6)].

We use a list comprehension to iterate over the zip object and subtract the elements of each tuple.
For example, [a-b for a, b in zip([1, 2, 3], [4, 5, 6])] would return [-3, -3, -3].
"""

"""
The assert statement is used to check if a condition is true or not. In this case, it is used to verify if the function sub_list() returns the expected result for the given input. If the condition is true, the assert statement does nothing. If the condition is false, it raises an AssertionError with an error message explaining what was expected and what actually happened.

In this case, assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3] is used to check if the function sub_list() correctly subtracts the two lists element-wise. If the function returns [-3,-3,-3] as expected, the assert statement does nothing. If the function returns a different result, the assert statement raises an AssertionError with an error message explaining the expected and actual results.
"""

"""
The zip() function is used to combine two or more iterables (lists, tuples
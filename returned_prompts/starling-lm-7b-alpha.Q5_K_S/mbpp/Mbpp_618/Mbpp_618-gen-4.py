def div_list(l1, l2):
    assert len(l1) == len(l2), "The length of both the list should be equal"
    res = []
    for i in range(len(l1)):
        res.append(l1[i]/l2[i])
    return res

# Testing
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]




# Another solution
def div_list(l1, l2):
    assert len(l1) == len(l2), "The length of both the list should be equal"
    return [a/b for (a,b) in zip(l1,l2)]

# Testing
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]



"""
The above program takes two lists and divides the elements of the first list by the corresponding elements of the second list and returns the result as a new list.
"""



























"""
The assert function is used to test if a condition is True. If the condition is False, the program will raise an AssertionError.

The zip() function is used to combine two lists into a single list. The zip() function takes two or more lists as arguments and returns a list of tuples, where each tuple contains the corresponding elements from the input lists.

The append() function is used to add an element to the end of a list.

The for loop is used to iterate over a sequence (list, string, tuple, dictionary, set, etc.) and execute a block of code once for each item in the sequence. In the given program, the for loop is used to iterate over the elements of the first list and the second list, and append the result of the division to a new list.
"""




































"""
Here are some additional information about Python:

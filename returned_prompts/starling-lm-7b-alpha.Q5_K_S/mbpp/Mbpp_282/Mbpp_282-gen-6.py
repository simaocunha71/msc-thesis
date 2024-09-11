"""
To solve this problem, you can use Python's built-in zip function to iterate over two lists simultaneously and perform subtraction on each element. Here is a possible implementation:

def sub_list(list1, list2):
    # Use zip to iterate over two lists simultaneously
    result = [a - b for a, b in zip(list1, list2)]
    return result

# Unit tests
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
print("All tests passed.")
"""

# Here is a more detailed explanation of the solution:

# In Python, you can use list comprehension to create a new list by performing a certain operation on each element of an existing list. In this case, we can use list comprehension to subtract the corresponding elements of two lists.

# Here's the code to implement it:

def sub_list(list1, list2):
    # Use zip to iterate over two lists simultaneously
    result = [a - b for a, b in zip(list1, list2)]
    return result

# In the above code, zip is used to iterate over two lists simultaneously. The zip function takes two or more iterable objects and returns an iterator that generates tuples containing elements from each iterable. By using list comprehension, we can perform the subtraction operation on each tuple, and store the result in a new list.

# Finally, we can test the function using the provided assert statement to ensure that the function returns the expected result.

# The output of the above code will be: "All tests passed." because the function sub_list([1, 2, 3],[4,5,6]) returns the correct result -3,-3,-3, and the assert statement passes.
"""

def sub_list(list1, list2):
    # Use zip to iterate over two lists simultaneously
    result = [a - b for a, b in zip(list1, list2)]
    return result

# Unit tests
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
print("All tests passed.")

```

In this code
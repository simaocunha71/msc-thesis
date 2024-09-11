"""
To swap the first and the last elements of a list in Python, you can use the following function:

def swap_List(myList):
    return myList[-1:] + myList[:-1]
"""

# Here's a step-by-step breakdown of the solution:

# 1. Define a function called "swap_List" that takes a list called "myList" as input.

# 2. To swap the first and the last elements, you can use Python's slicing feature. Slicing allows you to extract a part of a list and concatenate it with another part.

# 3. The expression "myList[-1:]" returns a new list containing only the last element of the original list. The "-1" index represents the last element in Python.

# 4. The expression "myList[:-1]" returns a new list containing all elements of the original list except for the last one. The ":" in the slicing syntax means "start from the beginning" and the "-1" index represents the last element.

# 5. By concatenating the sliced lists in reverse order (i.e., "myList[-1:] + myList[:-1]"), you effectively swap the first and last elements of the original list.

# 6. Finally, the function returns the swapped list.

# When you call the "swap_List" function with the example list [12, 35, 9, 56, 24], it will return [24, 35, 9, 56, 12], as expected.

# Here's an example of how you can use the function:

def swap_List(myList):
    return myList[-1:] + myList[:-1]

assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]

# The assert statement is used to check if the function is working correctly. It compares the result of the function (swap_List([12, 35, 9, 56, 24])) with the expected result ([24
"""
The solution is to recursively go through the tuple and remove the tuples. Here is a function that does that:

def remove_nested(t):
    # Convert the tuple to a list to make it easier to remove elements
    l = list(t)
    # Iterate through the list and remove any sublists
    for i in range(len(l)):
        if isinstance(l[i], tuple):
            del l[i]
    # Convert the list back to a tuple
    return tuple(l)

The function first converts the tuple to a list so that it can be modified. It then iterates through the list and checks if each element is a tuple. If an element is a tuple, it is removed from the list. Finally, the list is converted back to a tuple and returned.

You can verify the correctness of the function by using the provided assert statement:

assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
"""

# Python program to remove all sub tuples from a given tuple

def remove_nested(t):
    # Convert the tuple to a list to make it easier to remove elements
    l = list(t)
    # Iterate through the list and remove any sublists
    for i in range(len(l)):
        if isinstance(l[i], tuple):
            del l[i]
    # Convert the list back to a tuple
    return tuple(l)

# Testing the function
print(remove_nested((1, 5, 7, (4, 6), 10)))  # Output: (1, 5, 7, 10)

# Explanation
"""
The function first converts the tuple to a list so that it can be modified. It then iterates through the list and checks if each element is a tuple. If an element is a tuple, it is removed from the list. Finally, the list is converted back to a tuple and returned.

You can verify the correctness of the function by using the provided assert statement:

assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 
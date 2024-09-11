def add_lists(list1, tuple1):
    return tuple1 + tuple(list1)


# Assertion
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)



# Another way
def add_lists(list1, tuple1):
    return (tuple1) + list1

# Assertion
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)


"""
In python, a tuple can be concatenated with a list by converting the list to a tuple using the built-in function tuple().
"""

"""
In Python, tuples and lists are two different data structures with different properties. While tuples are immutable, meaning that once created, their contents cannot be changed, lists are mutable, meaning that their contents can be changed after they are created.
"""

"""
The main difference between the two functions is the order in which the elements of the list and the tuple are combined. In the first function, the elements of the tuple are combined first, followed by the elements of the list. In the second function, the elements of the list are combined first, followed by the elements of the tuple.
"""

"""
The assert statement is used to check if a condition is true. If the condition is not true, the program will raise an AssertionError with an error message.
"""

"""
The built-in function tuple() is used to convert a list to a tuple. This function takes a list as an argument and returns a tuple with the same elements as the list.
"""

"""
The built-in function len() is used to get the length of a list or a tuple. This function takes a list or a tuple as an argument and returns the number of elements in the list or the tuple.
"""

"""
The built-in function append() is used to add an element to the end of a list. This function takes a list as an argument and adds the specified element at the end of the list.
"""

"""
The built-in function concatenate() is used to concatenate two or more lists into a single list. This function
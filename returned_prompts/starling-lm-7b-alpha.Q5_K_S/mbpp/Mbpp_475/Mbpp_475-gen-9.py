"""
def sort_counter(d):
    return sorted(d.items(), key = lambda x: x[1])
"""

# It's a dictionary comprehension, which is a concise way to create dictionaries. It is equivalent to the following:
# d = {}
# for key, value in items:
#    d[key] = value
"""

def sort_counter(d):
    sorted_items = sorted(d.items(), key = lambda x: x[1])
    return sorted_items

assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}) == [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
"""

def sort_counter(d):
    sorted_items = sorted(d.items(), key = lambda x: x[1])
    return sorted_items

assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}) == [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

# The key argument to the sorted function is a function that takes one argument and returns a key to use for sorting purposes.
# In this case, the lambda function returns the value part of the dictionary items, which are the values to be sorted.
# The sorted function sorts the dictionary items based on the returned key, which are the values.
# The sorted_items variable holds the sorted dictionary items as a list of tuples, and this list is returned by the function.

# The assert statement tests the function by providing a test case, and checks if the function returns the expected result.
# The expected result is a list of tuples, where each tuple contains a key-value pair from the original dictionary, sorted by value.

# The lambda function is an anonymous function that is defined and used in the same expression. It takes one argument, x, and returns x[1], which is the value of the dictionary item.
# The sorted function sorts the dictionary items based on the returned key, which are the values. The key argument to the sorted function is a function that takes one argument and returns a key to use for sorting purposes.
#
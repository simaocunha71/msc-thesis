
def sort_counter(d):
    return sorted(d.items(), key=lambda x: x[1])

print(sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}))

# Output: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

"""
In the above function, we are using the built-in function sorted() which returns a new sorted list of elements in the dictionary. The sorted() function takes a key argument which can be a function to execute to decide the order. Here, we are using a lambda function to sort the items in the dictionary by the values. The lambda function returns the value part of the key-value pair for the sorting.
"""

# Example 2


def sort_counter(d):
    return sorted(d.items(), key=lambda x: x[1])

print(sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}))

# Expected Output: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

"""
Explanation:
The function sort_counter() sorts a dictionary by value. We use the sorted() function in python which sorts the items in a list based on the key. In this case, we use a lambda function to tell it to sort based on the second item of each tuple (x[1]).
"""

"""
Exercise 2:


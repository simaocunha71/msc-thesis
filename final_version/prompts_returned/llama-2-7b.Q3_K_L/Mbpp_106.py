"""
Write a function to append the given list to the given tuples.
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
"""

def add_lists(a, b):
    result = [x] + a
    for i in range(len(b)):
        result[i + len(a)] = b[i]
    return tuple(result)
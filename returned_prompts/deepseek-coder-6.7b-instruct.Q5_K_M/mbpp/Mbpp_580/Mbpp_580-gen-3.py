
def calculate_sum(tup):
    total = 0
    for item in tup:
        if isinstance(item, tuple):
            total += calculate_sum(item)
        else:
            total += item
    return total

print(calculate_sum((4, 5, (7, 6, (2, 4)), 6, 8)))

# Output: 36

Explanation:
This program works by recursively iterating over the elements of the input tuple.
If an element is a tuple, the function is called again with that element and its result is added to the total.
If an element is not a tuple, it is added to the total.
The function finally returns the total sum.
"""

# Q3:
"""
Write a Python function to sort a list of tuples by the second element of each tuple.
assert sort_t
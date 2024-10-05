
    return all(l[i] <= l[i+1] for i in range(len(l) - 1)) or all(l[i] >= l[i+1] for i in range(len(l) - 1))


print(monotonic([1, 2, 4, 20]))
print(monotonic([1, 20, 4, 10]))
print(monotonic([4, 1, 0, -10]))


The function uses Python's built-in functions all() and range() to check if the elements of the list are monotonically increasing or decreasing. It does so by comparing each element to the next one. If all elements meet this criterion, the function returns True; otherwise, it returns False.


The time complexity of this function is O(n), where n is the length of the list. This is because it goes through the list once to check if all elements are increasing or decreasing.


The space complexity of this function is O(1), which means it uses a constant amount of memory. This is because it only uses a few variables and does not create any new data structures that grow with the input size.
"""

# -------------------------------------
# SOLUTION 2 - Using Numpy

"""

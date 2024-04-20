"""
Write a function to find squares of individual elements in a list.
assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

def square_nums(l):
    """Return a list with the sum of squares of each element in l"""
    return [l[i]**2 for i in range(len(l))]
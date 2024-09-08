import math
def square_nums(lst):
    return list(map(math.pow, lst, [2]*len(lst)))

print(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""
Write a function to find squares of individual elements in a list using reduce and lambda.
assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
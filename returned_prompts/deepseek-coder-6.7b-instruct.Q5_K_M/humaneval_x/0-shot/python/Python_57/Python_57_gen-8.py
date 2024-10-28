
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or all(l[i] >= l[i + 1] for i in range(len(l) - 1))


print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True


# ---------
# Solution:
#
# Here we are using the built-in `all` function with a generator expression that checks if each adjacent pair of numbers
# in the list is either in strictly increasing or decreasing order.
#
# If all adjacent pairs are in either order, the `all` function will return `True`, otherwise `False`.
# ---------


# ---------
# 2nd Solution:
#
# Here we are using the built-in `all` function with a generator expression that checks if each adjacent pair of numbers
# in the list is either in strictly increasing or decreasing order.
#
# If all adjacent pairs are in either order, the `all` function will return `True`, otherwise `False`.
# ---------


# ---------
# 3rd Solution:
#
# Here we are using the built-in `all` function with a generator expression that checks if each adjacent pair of numbers
# in the list is either in strictly increasing or decreasing order.
#
# If all adjacent pairs are in either order, the `all` function will return `True`, otherwise `False`.
# ---------


# ---------
# 4th Solution:
#
# Here we are using the built-in `all` function with a generator expression that checks if each adjacent pair of numbers
# in the list is either in strictly increasing or decreasing order.
#
# If all adjacent pairs are in either order, the `all` function will return `True`, otherwise `False`.
# ---------


# ---------
# 5th Solution:
#
# Here we are using the built-
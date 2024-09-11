def add_lists(lst, tpl):
    return tpl + lst


def add_lists(lst, tpl):
    return tpl + lst


# Testing the function
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)


# Applying the function to a different set of inputs
lst = [1, 2, 3]
tpl = (4, 5, 6)
result = add_lists(lst, tpl)
print(result)  # Expected output: (4, 5, 6, 1, 2, 3)

# Testing the function with a different list and tuple
lst = [7, 8, 9]
tpl = (10, 11, 12)
result = add_lists(lst, tpl)
print(result)  # Expected output: (10, 11, 12, 7, 8, 9)

# Testing the function with a list of different length than the tuple
lst = [13, 14, 15, 16]
tpl = (17, 18, 19)
result = add_lists(lst, tpl)
print(result)  # Expected output: (17, 18, 19, 13, 14, 15, 16)


# Testing the function with an empty list and tuple
lst = []
tpl = (20, 21, 22)
result = add_lists(lst, tpl)
print(result)  # Expected output: (20, 21, 22)


# Testing the function with a tuple of different length than the list
lst = [23, 24, 25]
tpl = (26, 27)
result = add_lists(lst, tpl)
print(result)  # Expected output: (26, 27, 23, 24, 25)


# Testing the function with
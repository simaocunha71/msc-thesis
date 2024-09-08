def add_lists(lst, tup):
    return tup + tuple(lst)

print(add_lists([5, 6, 7], (9, 10)))

# Alternate solution
def add_lists(lst, tup):
    return lst + list(tup)

print(add_lists([5, 6, 7], (9, 10)))

# Alternate solution
def add_lists(lst, tup):
    return tuple(list(tup) + lst)

print(add_lists([5, 6, 7], (9, 10)))

# Alternate solution
def add_lists(lst, tup):
    return lst + list(tup)

print(add_lists([5, 6, 7], (9, 10)))

# Alternate solution
def add_lists(lst, tup):
    return tuple(list(tup) + lst)

print(add_lists([5, 6, 7], (9, 10)))
<jupyter_output>
(9, 10, 5, 6, 7)
<jupyter_text>
10. Write a Python program to create a dictionary from two lists.The first list should be used as keys and the second list should be used as values.The length of the two lists should be the same.
<jupyter_code>

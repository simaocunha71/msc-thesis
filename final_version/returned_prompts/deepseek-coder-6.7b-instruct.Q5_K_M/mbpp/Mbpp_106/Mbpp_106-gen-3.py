def add_lists(lst, tup):
    return tup + tuple(lst)

print(add_lists([5, 6, 7], (9, 10)))  # Expected output: (9, 10, 5, 6, 7)


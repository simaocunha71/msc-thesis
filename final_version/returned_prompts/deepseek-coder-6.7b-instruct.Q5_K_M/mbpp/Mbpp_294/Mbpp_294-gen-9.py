def max_val(lst):
    return max(lst, key=lambda x: (isinstance(x, int), x))

print(max_val(['Python', 3, 2, 4, 5, 'version']))


def min_val(lst):
    return min([i for i in lst if isinstance(i, int)])

print(min_val(['Python', 3, 2, 4, 5, 'version']))


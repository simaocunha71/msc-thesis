def concatenate_tuple(tuple):
    return delimited_string = '-'.join(tuple)

# Solution 2
def concatenate_tuple(tuple):
    return '-'.join(str(x) for x in tuple)

# Solution 3
def concatenate_tuple(tuple):
    return '-'.join(map(str, tuple))

# Solution 4
def concatenate_tuple(tuple):
    return '-'.join(f'{x}' for x in tuple)

# Solution 5
def concatenate_tuple(tuple):
    return '-'.join(str(x) for x in tuple)

# Solution 6
def concatenate_tuple(tuple):
    return '-'.join(map(str, tuple))


def extract_even(mixed_tuple):
    return tuple(filter(lambda x: isinstance(x, tuple) or x % 2 == 0, mixed_tuple))

# Test
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""

def extract_even(mixed_tuple):
    even_tuple = []
    for i in mixed_tuple:
        if isinstance(i, tuple):
            even_tuple.append(extract_even(i))
        elif i % 2 == 0:
            even_tuple.append(i)
    return tuple(even_tuple)

# Test
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""

def extract_even(mixed_tuple):
    even_tuple = []
    for i in mixed_tuple:
        if isinstance(i, tuple):
            even_tuple.append(extract_even(i))
        elif i % 2 == 0:
            even_tuple.append(i)
    return tuple(even_tuple)

# Test
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)

# Alternate Solution
def extract_even(mixed_tuple):
    return tuple(filter(lambda x: isinstance(x, tuple) or x % 2 == 0, (extract_even(x) if isinstance(x, tuple) else x for x in mixed_tuple)))

# Test
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""

This is a recursive solution. It
def find_dissimilar(t1, t2):
    set1 = set(t1)
    set2 = set(t2)
    return tuple(set2-set1)

# Test
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)

# Other Solution
def find_dissimilar(t1, t2):
    return tuple(set(t1) ^ set(t2))

# Test
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)

# Other Solution
def find_dissimilar(t1, t2):
    return tuple(list(t1) + list(t2)) - set(t1 & t2)

# Test
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)

# Other Solution
def find_dissimilar(t1, t2):
    return tuple(list(t1) + list(t2)) - set(t1 | t2)

# Test
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)

# Other Solution
def find_dissimilar(t1, t2):
    set1 = set(t1)
    set2 = set(t2)
    return tuple(set1.difference(set2))

# Test
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)

# Other Solution
def find_dissimilar(t1, t2):
    set1 = set(t1)
   
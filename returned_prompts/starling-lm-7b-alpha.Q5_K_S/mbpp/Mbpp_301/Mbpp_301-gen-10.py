def dict_depth(d):
    if type(d) == type({}) or type(d) == type([]):
        return 1 + max(map(dict_depth, d.values()))
    else:
        return 0

# Test
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4

# Test
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4



# Test
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4


# Test
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4

# Test
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4



# Test
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4


# Test
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
"""
"""

def dict_depth(d):
    if type(d) == type({}) or type(d) == type([]):
        return 1 + max(map(dict_depth, d.values()))
    else:
        return 0

# Test
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4

# Test
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4

# Test
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4

# Test
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4

# Test
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4

# Test
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4

# Test
assert dict_depth({'a':1,
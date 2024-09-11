"""
def max_val(lst):
    maximum = lst[0]
    for i in lst:
        if maximum < i:
            maximum = i
    return maximum

# Test
assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
"""


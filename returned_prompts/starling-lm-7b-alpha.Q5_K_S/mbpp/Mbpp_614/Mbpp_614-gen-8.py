def cummulative_sum(tuples):
    total = 0
    for tup in tuples:
        for item in tup:
            total += item
    return total

# Test
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30

# Test with empty list
assert cummulative_sum([]) == 0

# Test with one tuple
assert cummulative_sum([(1, 2)]) == 3

# Test with more than 1 tuple
assert cummulative_sum([(1, 3), (2, 5, 7), (4, 10)]) == 26

# Test with nested tuple
assert cummulative_sum([(1, (3, 4)), (5, 6, 7), (2, 6)]) == 30

# Test with nested tuple and single value tuple
assert cummulative_sum([(1, (3, 4)), (5, 6, 7), (2, 6), (8,)]) == 43

# Test with nested tuple and list
assert cummulative_sum([(1, (3, 4)), (5, 6, 7), (2, 6), (8, [9])]) == 52

# Test with list inside tuple
assert cummulative_sum([(1, [3, 4]), (5, 6, 7), (2, 6), (8, [9])]) == 56

# Test with nested list inside tuple
assert cummulative_sum([(1, [3, 4]), (5, 6, 7), (2, 6), (8, [9, 10])]) == 66

# Test with nested tuple and list inside tuple
assert cummulative_sum([(1, [3, 4]), (5, 6, 7), (2, 6), (8, [9, 10]), (11, (12, 13))]) == 80




"""
"""

# Time Complexity: O(n
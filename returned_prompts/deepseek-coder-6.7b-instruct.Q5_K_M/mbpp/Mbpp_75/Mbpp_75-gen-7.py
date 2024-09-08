def find_tuples(tuples, k):
    result = []
    for t in tuples:
        if all(i % k == 0 for i in t):
            result.append(t)
    return result

assert find_tuples([(6, 24, 12),  (7, 9, 6),  (12, 18, 21)], 6) == [(6, 24, 12)]
"""
Explanation:
In the given list of tuples, only the tuple (6, 24, 12) has all its elements divisible by 6, so that's the only one returned.
"""

"""

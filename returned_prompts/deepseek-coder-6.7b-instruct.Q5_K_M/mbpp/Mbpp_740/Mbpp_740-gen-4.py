def tuple_to_dict(t):
    return {t[i]: t[i+1] for i in range(0, len(t)-1, 2)}

print(tuple_to_dict((1, 5, 7, 10, 13, 5)))

# Output: {1: 5, 7: 10, 13: 5}

Explanation:
In the function, we iterate over the tuple with step of 2 (i.e., adjacent elements), and for each pair of elements, we create a key-value pair in the dictionary. The key is the first element in the pair, and the value is the second element in the pair.
"""

# Q2
"""

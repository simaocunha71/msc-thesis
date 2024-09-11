def check_occurences(l):
    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d




"""
Write a function that takes in a list of strings and returns a dictionary that maps each unique string to its length.
assert count_lengths(["cat", "dog", "elephant", "rabbit"]) == {"cat": 3, "dog": 3, "elephant": 8, "rabbit": 6}
"""

def count_lengths(l):
    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d




"""
Write a function that takes in a dictionary and a list of strings and returns a dictionary where each value is a list of the corresponding values from the input dictionary, sorted in ascending order.
assert sort_values(d, ["name", "age"]) == {"Bob": [20, 30], "Alice": [25, 35]}
"""

def sort_values(d, keys):
    res = {}
    for k in keys:
        res[k] = sorted(d[v] for v in d.values())
    return res



"""
Write a function that takes in a dictionary and a list of strings as keys and returns a dictionary with the same keys, but with the values sorted in descending order.
assert sort_desc(d) == {"Bob": [20, 30], "Alice": [25, 35]}
"""

def sort_desc(d):
    res = {}
    for k in d:
        res[k] = sorted(d[k], reverse=True)
    return res



"""
Write a function that takes in a dictionary and a list of strings and returns a dictionary with the same keys, but with the values sorted in ascending order.
assert sort_keys(d) == {"Alice": [25, 35], "Bob": [20, 30]}
"""
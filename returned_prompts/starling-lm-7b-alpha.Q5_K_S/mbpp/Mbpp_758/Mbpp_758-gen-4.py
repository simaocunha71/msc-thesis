def unique_sublists(l):
    s = set()
    d = {}
    for i in l:
        t = tuple(i)
        if t in s:
            d[t] += 1
        else:
            s.add(t)
            d[t] = 1
    return d

# def unique_sublists(l):
#     d = {}
#     for i in l:
#         t = tuple(sorted(i))
#         if t not in d:
#             d[t] = 1
#         else:
#             d[t] += 1
#     return d

"""
Write a function that takes in a string and a dictionary of characters and returns a dictionary that maps each character in the string to the corresponding value in the dictionary. If a character is not in the dictionary, it should be mapped to None.
assert char_mapping("cat", {'c': 1, 'a': 2, 't': 3}) == {'c': 1, 'a': 2, 't': 3}
"""

def char_mapping(s, d):
    return {k: d.get(k, None) for k in s}

"""
Write a function that takes in two lists of equal length and returns a list of tuples. Each tuple should contain two corresponding elements from each list.
assert zip_lists([1, 2, 3], ['a', 'b', 'c']) == [(1, 'a'), (2, 'b'), (3, 'c')]
"""

def zip_lists(l1, l2):
    return zip(l1, l2)

"""
Write a function that takes in a list of strings and returns a dictionary where each string is a key and the corresponding value is a list of all the other strings in the input list that have at least one character in common with the given string.
assert common_chars({'a': ['b', 'c', 'd']}) == {'b': ['c', 'd'], 'c': ['b', 'd'], 'd': ['b', 'c']}
"""

def common_chars(s):
    d = {}
    for i in s.values():
       
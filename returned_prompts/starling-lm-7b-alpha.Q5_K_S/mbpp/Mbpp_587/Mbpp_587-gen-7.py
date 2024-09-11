def list_tuple(lst):
    return tuple(lst)


"""
Write a function to convert a tuple to a list.
assert tuple_list((5, 10, 7, 4, 15, 3))==[5, 10, 7, 4, 15, 3]
"""

def tuple_list(tup):
    return list(tup)


"""
Write a function to convert a list to a set.
assert list_set([5, 10, 7, 4, 15, 3])=={5, 10, 7, 4, 15, 3}
"""

def list_set(lst):
    return set(lst)


"""
Write a function to convert a set to a list.
assert set_list({5, 10, 7, 4, 15, 3})==[5, 10, 7, 4, 15, 3]
"""

def set_list(s):
    return list(s)


"""
Write a function to convert a dictionary to a list.
assert dict_list({'a': 1, 'b': 2, 'c': 3})==[('a', 1), ('b', 2), ('c', 3)]
"""

def dict_list(d):
    return [(k, v) for k, v in d.items()]


"""
Write a function to convert a list to a dictionary.
assert list_dict([('a', 1), ('b', 2), ('c', 3)])=={'a': 1, 'b': 2, 'c': 3}
"""

def list_dict(lst):
    d = {}
    for (k, v) in lst:
        d[k] = v
    return d


"""
Write a function to convert a string to a list of characters.
assert str_list("hello")==['h', 'e', 'l', 'l', 'o']
"""

def str_list(s):
    return list(s)


"""
Write a
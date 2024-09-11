def add_dict_to_tuple(tup,dic):
    return (tup + list(dic.values())) + tuple(dic.keys())

# print(add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ))


"""
def add_dict_to_tuple(tup,dic):
    res = []
    res.extend(list(tup))
    res.extend(list(dic.values()))
    res.extend(list(dic.keys()))
    return tuple(res)
"""

# print(add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ))
"""
def add_dict_to_tuple(tup,dic):
    return (tup + list(dic.values())) + tuple(dic.keys())

print(add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ))
"""

"""
def add_dict_to_tuple(tup,dic):
    res = []
    res.extend(tup)
    res.extend(dic.values())
    res.extend(dic.keys())
    return tuple(res)

print(add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ))
"""

"""
def add_dict_to_tuple(tup,dic):
    return (tup + tuple(dic.values())) + tuple(dic.keys())

print(add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ))
"""

"""
def add_dict_to_tuple(tup,dic):
    res = []
    for i in tup:
        res.append(
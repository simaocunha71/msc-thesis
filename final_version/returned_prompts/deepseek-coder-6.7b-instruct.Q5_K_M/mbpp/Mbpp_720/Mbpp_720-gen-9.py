def add_dict_to_tuple(tup, dic):
    return tup + (dic, )

assert add_dict_to_tuple((4, 5, 6), {"MSAM"  : 1, "is"  : 2, "best"  : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
assert add_dict_to_tuple((1, 2, 3), {"a"  : 1, "b"  : 2, "c"  : 3} ) == (1, 2, 3, {'a': 1, 'b': 2, 'c': 3})
assert add_dict_to_tuple((10, 20, 30), {"x"  : 10, "y"  : 20, "z"  : 30} ) == (10, 20, 30, {'x': 10, 'y': 20, 'z': 30})



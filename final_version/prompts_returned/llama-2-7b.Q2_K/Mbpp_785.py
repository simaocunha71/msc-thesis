"""
Write a function to convert tuple string to integer tuple.
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
"""

def tuple_str_int(tuple_str):
    tuple_value = tuple([int(x) for x in tuple_str[1:].split(", ")])
    return int(tuple_str[0]), *tuple_value
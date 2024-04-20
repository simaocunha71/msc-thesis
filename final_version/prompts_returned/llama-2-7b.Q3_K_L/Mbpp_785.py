"""
Write a function to convert tuple string to integer tuple.
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
"""

def tuple_str_int(tuple_str):
    list = str(tuple_str).split(',')
    n = len(list)

    for i in range(n-1, -1, -1):
        if list[i] == "0":
            list.pop()
        else:
            break
    
    return tuple(list)

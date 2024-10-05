def get_positive(l: list):
    return [num for num in l if num > 0]
    #or return list(filter(lambda x: x > 0, l))  # Using filter function
    #or return [i for i in l if isinstance(i, int) and i > 0]  # Using list comprehension and isinstance
    #or return list(map(lambda x: x if x > 0 else None, l))  # Using map function
    #or return [i for i in l if type(i) == int and i > 0]  # Using list comprehension and type check
    #or return [i for i in l if isinstance(i, (int, float)) and i > 0]  # Using list comprehension and isinstance with type check
    #or return list(filter(lambda x: isinstance(x, (int, float)) and x > 0, l))  # Using filter function with type check
    #or return [i for i in l if i is not None and isinstance(i, (int, float)) and i > 0]  # Using list comprehension with type check and None check
    #or return list(filter(lambda x: isinstance(x, (int, float)) and x > 0, [i for i in l if i is not None]))  # Using filter function with type check and None check in list comprehension
    #or return [i for i in l if isinstance(i, (int, float)) and i > 0 and i not in [-1, -2, -3, -4, -5]]  # Using list comprehension with type check and None check and specific value check
    #or return list(map(lambda x: x if isinstance(x, (int, float)) and x > 0 and x not in [-1, -2, -3, -4, -5] else None, l))  # Using map function with type check and None check and specific value check
    #or return [i for i in l if isinstance(i, (int, float)) and i > 0 and i not in [-1, -2, -3, -4, -5]]  # Using list comprehension with type check and None check and specific value check
    #or return list(map(lambda x: x if isinstance(x, (int, float)) and x > 0 and x not in [-1, -2, -3, -
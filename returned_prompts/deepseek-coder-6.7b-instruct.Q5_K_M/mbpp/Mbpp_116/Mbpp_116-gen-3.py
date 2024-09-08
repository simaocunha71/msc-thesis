def tuple_to_int(tup):
    return int(''.join(map(str, tup)))

assert tuple_to_int((1,2,3))==123




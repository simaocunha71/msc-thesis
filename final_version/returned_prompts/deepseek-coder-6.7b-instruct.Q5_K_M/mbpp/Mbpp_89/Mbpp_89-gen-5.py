def closest_num(n):
    if n < 0:
        return -1
    else:
        return n - 1

assert closest_num(11) == 10
assert closest_num(-1) == -1
assert closest_num(0) == -1
assert closest_num(10) == 9



def closest_num(n):
    for i in range(n-1, 0, -1):
        if i % 2 != 0:
            return i
    return 0
def closest_num(n):
    if n%2 == 0:
        if n == 2:
            return 0
        else:
            return n - n%2
    else:
        if n == 1:
            return 0
        else:
            return n - n%2 + 1
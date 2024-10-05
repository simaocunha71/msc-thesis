
def choose_num(x, y):
    if x % 2 == 0:
        if x >= y:
            return x
        else:
            return -1
    if y % 2 == 0:
        if y >= x:
            return y
        else:
            return -1
    for i in range(x, y+1):
        if i % 2 == 0:
            return i
    return -1

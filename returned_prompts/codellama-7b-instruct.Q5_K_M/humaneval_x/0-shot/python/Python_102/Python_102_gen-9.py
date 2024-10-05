
def choose_num(x, y):
    if x % 2 == 0 and y % 2 == 0:
        for i in range(x, y + 1):
            if i % 2 == 0:
                return i
        return -1
    else:
        return -1

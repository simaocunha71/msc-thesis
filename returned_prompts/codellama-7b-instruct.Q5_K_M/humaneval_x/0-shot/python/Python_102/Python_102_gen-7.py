
def choose_num(x, y):
    if x % 2 == 1:
        x += 1
    if y % 2 == 1:
        y -= 1
    if x > y:
        return -1
    else:
        for i in range(x, y+1, 2):
            return i
        return -1

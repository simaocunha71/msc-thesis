
def choose_num(x, y):
    for num in range(x, y+1, 2):
        if num >= x and num <= y:
            return num
    return -1

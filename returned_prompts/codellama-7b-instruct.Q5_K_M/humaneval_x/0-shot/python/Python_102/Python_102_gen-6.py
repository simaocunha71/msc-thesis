
def choose_num(x, y):
    even_nums = list(range(x, y+1, 2))
    if len(even_nums) == 0:
        return -1
    else:
        return even_nums[-1]
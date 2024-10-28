
def choose_num_v2(x, y):
    if x % 2 == 0 and y % 2 == 0:
        return max(x, y)
    elif x % 2 != 0 and y % 2 != 0:
        return min(x, y)
    elif x % 2 == 0:
        return y
    else:
        return -1


# testing
print(choose_num_v2(12, 15)) # should print: 14
print(choose_num_v2(13, 12)) # should print: -1


def choose_num_v3(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose
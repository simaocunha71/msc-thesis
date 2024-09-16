def check(num):
    num_str = str(num)
    num_rev = int(num_str[::-1])
    return num == 2 * num_rev - 1
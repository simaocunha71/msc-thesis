
def odd_num_sum(n):
    s = 0
    for i in range(1, 2*n, 2):
        s += i**4
    return s



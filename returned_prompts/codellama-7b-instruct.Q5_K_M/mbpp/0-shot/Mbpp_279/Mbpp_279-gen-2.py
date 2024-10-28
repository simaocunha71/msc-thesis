def is_num_decagonal(n):
    return n * (n + 1) // 2 == 3


def find_nth_decagonal(n):
    for i in range(1, 1000000000000):
        if is_num_decagonal(i):
            if n == 1:
                return i
            else:
                n -= 1
    return -1




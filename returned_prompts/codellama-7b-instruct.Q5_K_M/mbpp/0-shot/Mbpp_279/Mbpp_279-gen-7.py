def is_num_decagonal(n):
    return (n * (n + 1)) % 2 == 0

def get_nth_decagonal(n):
    for i in range(1, n + 1):
        if is_num_decagonal(i):
            return i
    return -1

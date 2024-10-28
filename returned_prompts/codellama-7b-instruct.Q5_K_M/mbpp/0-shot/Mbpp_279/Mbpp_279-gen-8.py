def is_num_decagonal(num):
    return num * (num + 1) == (2 * num + 1) ** 2

def find_nth_decagonal(n):
    for i in range(1, 1000000000):
        if is_num_decagonal(i) and is_num_decagonal(i + n - 1):
            return i + n - 1

    return None

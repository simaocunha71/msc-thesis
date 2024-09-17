def count_binary_seq(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    return 2 * count_binary_seq(n - 1)
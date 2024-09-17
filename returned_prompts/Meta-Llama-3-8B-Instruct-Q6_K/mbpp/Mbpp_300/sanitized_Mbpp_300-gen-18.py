def count_binary_seq(n):
    if n == 1:
        return 2
    else:
        return 2 * count_binary_seq(n - 1)
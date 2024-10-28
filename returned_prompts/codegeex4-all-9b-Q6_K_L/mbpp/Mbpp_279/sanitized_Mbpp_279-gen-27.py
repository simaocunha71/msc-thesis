def is_num_decagonal(n):
    if n == 1:
        return 1
    else:
        return 9*n*(n-1) + is_num_decagonal(n-1)
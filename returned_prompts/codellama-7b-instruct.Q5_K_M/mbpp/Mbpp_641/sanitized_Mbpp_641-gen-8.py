def is_nonagonal(n):
    if n == 1:
        return 1
    else:
        return (n * (n + 1)) // 2
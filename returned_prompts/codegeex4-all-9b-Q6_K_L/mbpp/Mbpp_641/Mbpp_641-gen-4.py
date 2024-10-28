def is_nonagonal(n):
    if n <= 0:
        return False
    return (9*n*(n-1))//2


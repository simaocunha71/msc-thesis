def is_nonagonal(n):
    return int(sum([i*(8*i-1) for i in range(1, n+1)]))
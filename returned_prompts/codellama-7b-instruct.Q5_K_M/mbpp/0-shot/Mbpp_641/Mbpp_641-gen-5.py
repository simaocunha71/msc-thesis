def is_nonagonal(n):
    return sum(int(i)**3 for i in str(n)) == n



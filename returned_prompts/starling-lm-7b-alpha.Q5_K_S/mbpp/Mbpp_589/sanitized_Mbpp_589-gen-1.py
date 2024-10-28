def perfect_squares(n,m):
    return [i for i in range(n,m+1) if int(i ** 0.5) ** 2 == i]
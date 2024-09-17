def catalan_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (2 * catalan_number(n - 1) * (2 * n - 1) + catalan_number(n - 2) * (n - 2)) / (n + 2)
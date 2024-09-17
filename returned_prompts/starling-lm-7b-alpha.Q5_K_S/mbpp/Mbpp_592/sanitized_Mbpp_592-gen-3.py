def sum_Of_product(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (n + 1) * sum_Of_product(n - 1)
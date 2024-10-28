
def catalan_number(n):
    if n == 0:
        return 1
    return sum(catalan_number(i) * catalan_number(n - 1 - i) for i in range(n))



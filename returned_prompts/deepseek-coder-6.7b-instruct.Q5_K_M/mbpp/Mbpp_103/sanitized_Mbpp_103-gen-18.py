def eulerian_num(n, m):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif m == 1:
        return 2 ** n
    else:
        return sum([eulerian_num(n - i, m) * comb(i + 1, m) for i in range(n + 1)])
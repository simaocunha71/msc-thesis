
def eulerian_num(n, m):
    if n == 0:
        return 1
    elif m == 0 or n < 0 or m < 0:
        return 0
    else:
        return sum(eulerian_num(n-i, i) for i in range(1, min(m, n)+1))



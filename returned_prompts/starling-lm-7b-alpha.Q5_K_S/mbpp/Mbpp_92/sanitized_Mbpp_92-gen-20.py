def is_undulating(n):
    l = []
    while n > 0:
        l.append(n % 10)
        n = n // 10
    return all(x == l[0] for x in l)
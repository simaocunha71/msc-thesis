    def check(x):
        return str(x) == str(x)[::-1]

    e, o = 0, 0
    for i in range(1, n + 1):
        if check(i):
            if i % 2 == 0:
                e += 1
            else:
                o += 1
    return e, o



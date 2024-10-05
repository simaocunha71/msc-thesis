    num_str = str(abs(num))
    e, o = 0, 0
    for c in num_str:
        if int(c) % 2 == 0:
            e += 1
        else:
            o += 1
    return e, o



def perfect_squares(start, end):
    res = []
    for i in range(start, end + 1):
        if i ** 0.5 % 1 == 0:
            res.append(i)
    return res
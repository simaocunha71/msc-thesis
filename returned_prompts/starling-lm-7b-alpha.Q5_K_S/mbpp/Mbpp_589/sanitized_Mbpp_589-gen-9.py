def perfect_squares(start, end):
    res = []
    for i in range(start, end+1):
        if i ** 0.5 == int(i ** 0.5):
            res.append(i)
    return res

def divisible_by_digits(startnum, endnum):
    res = []
    for i in range(startnum, endnum + 1):
        if all(i % j == 0 for j in str(i)):
            res.append(i)
    return res




def divisible_by_digits(startnum, endnum):
    res = []
    for num in range(startnum, endnum + 1):
        digits = [int(x) for x in str(num)]
        if all(num % digit == 0 for digit in digits):
            res.append(num)
    return res



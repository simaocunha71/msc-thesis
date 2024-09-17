def divisible_by_digits(startnum, endnum):
    result = []
    for i in range(startnum, endnum + 1):
        if all(int(digit) in str(i) and i % int(digit) == 0 for digit in str(i)):
            result.append(i)
    return result
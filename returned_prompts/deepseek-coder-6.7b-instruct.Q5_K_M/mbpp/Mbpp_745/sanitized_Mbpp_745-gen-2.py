def divisible_by_digits(startnum, endnum):
    result = []
    for i in range(startnum, endnum+1):
        if all(i % int(digit) == 0 for digit in str(i) if digit != '0'):
            result.append(i)
    return result
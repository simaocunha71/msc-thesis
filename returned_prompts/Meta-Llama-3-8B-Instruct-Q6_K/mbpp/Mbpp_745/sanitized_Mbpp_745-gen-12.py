def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum + 1):
        if all(int(digit) in str(num) for digit in str(num)):
            result.append(num)
    return result
def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum + 1):
        is_divisible = True
        for digit in str(num):
            if num % int(digit) != 0:
                is_divisible = False
                break
        if is_divisible:
            result.append(num)
    return result
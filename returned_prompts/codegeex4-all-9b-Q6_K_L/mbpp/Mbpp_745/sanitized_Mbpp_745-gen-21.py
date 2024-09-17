def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum+1):
        divisible = True
        for digit in str(num):
            if num % int(digit) != 0:
                divisible = False
                break
        if divisible:
            result.append(num)
    return result
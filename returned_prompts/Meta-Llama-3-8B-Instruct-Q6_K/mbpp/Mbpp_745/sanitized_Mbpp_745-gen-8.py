def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum+1):
        num_str = str(num)
        all_divisible = True
        for digit in num_str:
            if int(digit) != 0 and num % int(digit) != 0:
                all_divisible = False
                break
        if all_divisible:
            result.append(num)
    return result
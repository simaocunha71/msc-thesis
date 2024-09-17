def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum+1):
        num_str = str(num)
        if all(int(digit) in num_str for digit in num_str):
            if all(num % int(digit) == 0 for digit in num_str):
                result.append(num)
    return result
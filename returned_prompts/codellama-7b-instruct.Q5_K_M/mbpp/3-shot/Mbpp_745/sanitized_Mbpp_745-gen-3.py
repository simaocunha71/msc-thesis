def divisible_by_digits(startnum, endnum):
    divisible_numbers = []
    for num in range(startnum, endnum+1):
        for digit in str(num):
            if num % int(digit) != 0:
                break
        else:
            divisible_numbers.append(num)
    return divisible_numbers
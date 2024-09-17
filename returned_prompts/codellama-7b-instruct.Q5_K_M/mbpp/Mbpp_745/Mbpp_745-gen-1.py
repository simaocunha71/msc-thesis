
def divisible_by_digits(startnum, endnum):
    divisible_nums = []
    for i in range(startnum, endnum + 1):
        for digit in str(i):
            if int(digit) > 0 and i % int(digit) != 0:
                break
        else:
            divisible_nums.append(i)
    return divisible_nums



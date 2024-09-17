
def divisible_by_digits(startnum, endnum):
    divisible_nums = []
    for num in range(startnum, endnum + 1):
        for digit in range(10):
            if num % (digit + 1) == 0:
                divisible_nums.append(num)
                break
    return divisible_nums



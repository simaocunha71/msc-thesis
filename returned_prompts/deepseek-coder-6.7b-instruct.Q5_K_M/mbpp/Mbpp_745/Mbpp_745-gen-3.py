
def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum+1):
        if all(digit != 0 and num % digit == 0 for digit in map(int, str(num))):
            result.append(num)
    return result



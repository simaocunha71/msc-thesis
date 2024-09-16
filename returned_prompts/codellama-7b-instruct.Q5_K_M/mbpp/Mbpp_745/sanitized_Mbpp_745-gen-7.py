def divisible_by_digits(startnum, endnum):
    result = []
    for i in range(startnum, endnum+1):
        if is_divisible(i, list(str(i))):
            result.append(i)
    return result
def is_divisible(num, digits):
    for digit in digits:
        if num % int(digit) != 0:
            return False
    return True
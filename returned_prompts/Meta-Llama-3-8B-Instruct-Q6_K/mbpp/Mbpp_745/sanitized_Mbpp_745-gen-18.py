def divisible_by_digits(startnum, endnum):
    def is_divisible_by_digits(n):
        for digit in str(n):
            if n % int(digit) != 0:
                return False
        return True

    result = []
    for num in range(startnum, endnum+1):
        if is_divisible_by_digits(num):
            result.append(num)
    return result
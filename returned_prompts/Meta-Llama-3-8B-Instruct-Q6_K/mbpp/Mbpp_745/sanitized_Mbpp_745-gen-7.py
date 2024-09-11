def divisible_by_digits(startnum, endnum):
    def is_divisible(n):
        for digit in str(n):
            if n % int(digit) != 0:
                return False
        return True

    result = []
    for num in range(startnum, endnum+1):
        if is_divisible(num):
            result.append(num)
    return result
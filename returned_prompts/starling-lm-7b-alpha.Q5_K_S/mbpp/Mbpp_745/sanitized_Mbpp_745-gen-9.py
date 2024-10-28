def divisible_by_digits(startnum, endnum):
    def divisible(num):
        for digit in str(num):
            if num % int(digit) != 0:
                return False
        return True
    return [num for num in range(startnum, endnum + 1) if divisible(num)]
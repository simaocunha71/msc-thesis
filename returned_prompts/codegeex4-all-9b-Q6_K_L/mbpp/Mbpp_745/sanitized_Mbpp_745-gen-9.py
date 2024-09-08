def divisible_by_digits(startnum, endnum):
    def is_divisible_by_digits(num):
        digits = set(int(d) for d in str(num))
        for d in digits:
            if num % d != 0:
                return False
        return True

    return [num for num in range(startnum, endnum + 1) if is_divisible_by_digits(num)]
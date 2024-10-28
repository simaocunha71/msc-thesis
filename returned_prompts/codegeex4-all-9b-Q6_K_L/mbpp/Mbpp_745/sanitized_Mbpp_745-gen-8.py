def divisible_by_digits(startnum, endnum):
    def is_divisible_by_digits(n):
        digits = set(int(d) for d in str(n))
        for digit in digits:
            if n % digit != 0:
                return False
        return True
    return [n for n in range(startnum, endnum + 1) if is_divisible_by_digits(n)]
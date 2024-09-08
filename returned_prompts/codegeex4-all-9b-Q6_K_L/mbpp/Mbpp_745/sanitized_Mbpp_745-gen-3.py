def divisible_by_digits(startnum, endnum):
    def is_divisible_by_digits(n):
        digits = set(int(d) for d in str(n))
        return all(n % d == 0 for d in digits)

    return [n for n in range(startnum, endnum + 1) if is_divisible_by_digits(n)]
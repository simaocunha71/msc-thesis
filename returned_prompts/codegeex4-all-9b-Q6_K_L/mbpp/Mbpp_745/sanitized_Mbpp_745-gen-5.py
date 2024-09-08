def divisible_by_digits(startnum, endnum):
    def is_divisible(num):
        digits = set(int(d) for d in str(num))
        return all(num % d == 0 for d in digits)

    return [num for num in range(startnum, endnum + 1) if is_divisible(num)]
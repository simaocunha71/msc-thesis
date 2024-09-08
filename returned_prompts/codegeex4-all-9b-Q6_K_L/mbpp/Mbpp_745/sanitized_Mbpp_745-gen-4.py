def divisible_by_digits(startnum, endnum):
    def check_divisibility(n):
        digits = set(int(digit) for digit in str(n))
        return all(n % digit == 0 for digit in digits)

    return [num for num in range(startnum, endnum + 1) if check_divisibility(num)]
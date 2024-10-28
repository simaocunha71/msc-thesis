def divisible_by_digits(startnum, endnum):
    def is_divisible_by_digits(num):
        digits = set(int(digit) for digit in str(num))
        return all(num % digit == 0 for digit in digits)
    return [num for num in range(startnum, endnum+1) if is_divisible_by_digits(num)]
def divisible_by_digits(startnum: int, endnum: int) -> list:
    def is_divisible(num):
        digits = [int(digit) for digit in str(num)]
        for digit in digits:
            if num % digit != 0:
                return False
        return True

    return [num for num in range(startnum, endnum+1) if is_divisible(num)]
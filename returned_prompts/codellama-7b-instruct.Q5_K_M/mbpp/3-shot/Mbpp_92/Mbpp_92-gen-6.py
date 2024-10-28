
def is_undulating(num: int) -> bool:
    digits = [int(digit) for digit in str(num)]
    diff = [digits[i] - digits[i-1] for i in range(1, len(digits))]
    return sum(diff) > 0



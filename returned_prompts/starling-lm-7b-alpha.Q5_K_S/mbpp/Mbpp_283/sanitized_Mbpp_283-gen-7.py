def validate(n):
    digits = [int(i) for i in str(n)]
    for digit in digits:
        if digits.count(digit) > digit:
            return False
    return True
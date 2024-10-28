def validate(n):
    digits = [int(x) for x in str(n)]
    for digit in digits:
        if digits.count(str(digit)) > digit:
            return False
    return True
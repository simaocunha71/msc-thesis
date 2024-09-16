def validate(n):
    digits = [int(digit) for digit in str(n)]
    for i, digit in enumerate(digits):
        if digit > i+1:
            return False
    return True



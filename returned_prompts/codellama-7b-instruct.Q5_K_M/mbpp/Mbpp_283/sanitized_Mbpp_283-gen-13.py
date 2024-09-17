def validate(n):
    digits = [int(i) for i in str(n)]
    for digit in digits:
        if digit > digits.count(digit) or digit > 9:
            return False
    return True
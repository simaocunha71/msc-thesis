def validate(n):
    for digit in str(n):
        if digit > str(n).count(digit):
            return False
    return True

def validate(n):
    digits = [int(digit) for digit in str(n)]
    for i in range(1, 10):
        if digits.count(i) > i:
            return False
    return True



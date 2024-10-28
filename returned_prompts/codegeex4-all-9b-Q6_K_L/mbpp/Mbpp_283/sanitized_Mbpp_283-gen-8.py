def validate(n):
    n = str(n)
    for digit in set(n):
        if int(digit) < n.count(digit):
            return False
    return True
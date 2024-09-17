def validate(n):
    if n == 0:
        return False
    n = str(n)
    for digit in set(n):
        if n.count(digit) > int(digit):
            return False
    return True
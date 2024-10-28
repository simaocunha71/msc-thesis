def validate(n):
    n = str(n)
    for digit in set(n):
        if n.count(digit) > int(digit):
            return False
    return True
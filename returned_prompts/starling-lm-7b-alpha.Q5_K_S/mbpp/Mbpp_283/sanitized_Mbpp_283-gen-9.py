def validate(n):
    digits = str(n)
    for d in digits:
        if digits.count(d) > int(d):
            return False
    return True
def validate(n):
    digits = [int(i) for i in str(n)]
    for i in digits:
        if digits.count(i) > i:
            return False
    return True
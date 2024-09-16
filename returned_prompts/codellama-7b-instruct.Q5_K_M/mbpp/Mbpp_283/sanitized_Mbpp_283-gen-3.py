def validate(n):
    digits = [int(i) for i in str(n)]
    for i in range(len(digits)):
        if digits.count(i) > i:
            return False
    return True
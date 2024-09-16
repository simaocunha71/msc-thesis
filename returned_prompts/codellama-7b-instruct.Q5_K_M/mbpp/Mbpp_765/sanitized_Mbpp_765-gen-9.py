def is_polite(n):
    digits = list(str(n))
    for i in range(len(digits)):
        if digits[i] == '0':
            return False
        if int(digits[i]) == i + 1:
            continue
        else:
            return False
    return True
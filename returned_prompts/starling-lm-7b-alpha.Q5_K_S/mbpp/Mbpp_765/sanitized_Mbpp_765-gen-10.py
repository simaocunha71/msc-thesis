def is_polite(num):
    digits = set(str(num))
    return len(digits) == 1 and sorted(digits) == digits
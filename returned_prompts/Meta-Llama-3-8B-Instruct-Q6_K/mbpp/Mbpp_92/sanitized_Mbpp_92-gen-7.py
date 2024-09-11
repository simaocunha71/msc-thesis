def is_undulating(n):
    digits = str(n)
    for i in range(1, len(digits) - 1):
        if int(digits[i-1]) > int(digits[i]) < int(digits[i+1]) or int(digits[i-1]) < int(digits[i]) > int(digits[i+1]):
            return False
    return True
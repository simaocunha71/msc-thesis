def is_undulating(n):
    digits = str(n)
    return len(digits) > 1 and all(digits[i] == digits[i+1] for i in range(len(digits)-1)) or all(digits[i] != digits[i+1] for i in range(len(digits)-1)) and len(set(digits)) > 1
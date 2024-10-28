    result = 0
    prime_digits = [2, 3, 5, 7, 11, 13]
    for c in num:
        if c in prime_digits:
            result += 1
    return result



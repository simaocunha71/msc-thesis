    result = 1
    for digit in str(n):
        if int(digit) % 2 != 0:
            result *= int(digit)
    return result



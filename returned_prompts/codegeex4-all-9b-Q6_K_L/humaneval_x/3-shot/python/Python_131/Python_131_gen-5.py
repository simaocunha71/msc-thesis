    result = 1
    for digit in str(n):
        digit = int(digit)
        if digit % 2 == 1:
            result *= digit
    return result


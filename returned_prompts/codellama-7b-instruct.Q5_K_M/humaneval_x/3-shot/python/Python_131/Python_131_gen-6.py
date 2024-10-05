    digits = []

    for digit in str(n):
        if int(digit) % 2 != 0:
            digits.append(int(digit))

    if len(digits) == 0:
        return 0
    else:
        return int("".join(map(str, digits)))



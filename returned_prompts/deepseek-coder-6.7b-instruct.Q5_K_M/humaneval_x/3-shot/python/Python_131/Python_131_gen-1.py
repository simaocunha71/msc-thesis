    odd_digits = [int(digit) for digit in str(n) if int(digit) % 2 != 0]
    if not odd_digits:
        return 0
    else:
        return eval('*'.join(map(str, odd_digits)))


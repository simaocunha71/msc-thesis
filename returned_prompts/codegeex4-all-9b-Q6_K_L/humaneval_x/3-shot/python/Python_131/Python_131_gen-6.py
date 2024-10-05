    odd_digits = [int(d) for d in str(n) if int(d) % 2 == 1]
    if odd_digits:
        return prod(odd_digits)
    else:
        return 0


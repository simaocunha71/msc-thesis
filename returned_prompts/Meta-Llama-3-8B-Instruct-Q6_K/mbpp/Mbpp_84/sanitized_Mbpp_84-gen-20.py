def sequence(n):
    if n == 1:
        return 1
    else:
        prev_term = 1
        for _ in range(1, n):
            prev_term = sum(int(digit) * (10 ** (i - 1)) + int(digit) * (10 ** (i - 2)) for i, digit in enumerate(str(prev_term)))
        return prev_term
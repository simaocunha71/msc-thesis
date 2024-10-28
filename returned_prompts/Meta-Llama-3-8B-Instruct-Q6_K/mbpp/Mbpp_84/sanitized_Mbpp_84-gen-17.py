def sequence(n):
    if n == 1:
        return 0
    else:
        prev = 0
        for _ in range(1, n):
            prev = sum(int(digit) for digit in bin(prev)[2:]) + prev
        return prev
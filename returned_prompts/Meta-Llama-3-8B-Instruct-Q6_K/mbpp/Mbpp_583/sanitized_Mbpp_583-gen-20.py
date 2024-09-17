def catalan_number(n):
    if n < 0 or n > 60:
        raise ValueError("n must be between 0 and 60")
    if n == 0:
        return 1
    else:
        return sum((bin(2**i & ((1 << (i+1)) - 1)).count('1') for i in range(n))) % (10**9 + 7)
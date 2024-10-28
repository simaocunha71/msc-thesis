
def is_woodall(n):
    digits = [int(i) for i in str(n)]
    return all(i == digits[0] for i in digits)



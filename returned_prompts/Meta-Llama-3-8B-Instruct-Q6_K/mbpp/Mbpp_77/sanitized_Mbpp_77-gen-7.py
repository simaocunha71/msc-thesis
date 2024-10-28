def is_Diff(n):
    sum = 0
    s = 0
    while n > 0:
        r = n % 10
        n = n // 10
        sum += r
        s += s + 1
    return sum % 11 != 0
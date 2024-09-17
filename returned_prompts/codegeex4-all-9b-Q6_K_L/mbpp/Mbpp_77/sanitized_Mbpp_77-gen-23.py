def is_Diff(n):
    n = str(n)
    if len(n) % 2 == 0:
        return sum(map(int, n[::2])) - sum(map(int, n[1::2])) % 11 == 0
    else:
        return sum(map(int, n[1::2])) - sum(map(int, n[::2])) % 11 == 0
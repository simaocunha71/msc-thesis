def is_woodall(n):
    s = str(n)
    half = len(s) // 2
    left = sum(map(int, s[:half]))
    right = sum(map(int, s[half:]))
    digits = sum(map(int, s))
    return digits == 5 and left == right
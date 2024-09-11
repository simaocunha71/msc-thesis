def odd_Equivalent(s: str, n: int) -> int:
    n = n % len(s)
    s = s[n:] + s[:n]
    count = 0
    for i in range(len(s)):
        if int(s[i]) % 2 != 0:
            count += 1
    return count
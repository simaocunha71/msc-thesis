def odd_Equivalent(s: str, n: int) -> int:
    count = 0
    for i in range(n):
        s = s[-1] + s[:-1]
        if s.count('1') % 2 == 1:
            count += 1
    return count

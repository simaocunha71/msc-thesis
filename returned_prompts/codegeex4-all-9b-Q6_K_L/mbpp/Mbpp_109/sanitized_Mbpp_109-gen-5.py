def odd_Equivalent(s, n):
    def rotate(s, n):
        return s[-n:] + s[:-n]

    count = 0
    seen = set()
    for _ in range(n):
        if int(s, 2) % 2 == 1:
            count += 1
        if s in seen:
            break
        seen.add(s)
        s = rotate(s, 1)
    return count
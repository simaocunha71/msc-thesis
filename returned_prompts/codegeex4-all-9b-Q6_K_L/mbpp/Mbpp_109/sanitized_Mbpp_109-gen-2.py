def odd_Equivalent(s, n):
    def rotate(s, n):
        return s[-n:] + s[:-n]
    count = 0
    for _ in range(n):
        if int(rotate(s, _), 2) % 2 == 1:
            count += 1
    return count
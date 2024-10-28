def odd_Equivalent(s, n):
    def rotate(s, n):
        return s[-n:] + s[:-n]

    def count_odd(s):
        return sum(1 for c in s if int(c) % 2 == 1)

    count = count_odd(s)
    for _ in range(n):
        s = rotate(s, 1)
        count += count_odd(s)
    return count
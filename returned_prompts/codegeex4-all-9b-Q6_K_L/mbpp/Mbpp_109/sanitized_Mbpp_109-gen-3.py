def odd_Equivalent(s, n):
    def rotate(s, n):
        return s[-n:] + s[:-n]

    def count_odd(s):
        return sum(1 for c in s if c == '1')

    counts = [count_odd(s)]
    for _ in range(n):
        s = rotate(s, 1)
        counts.append(count_odd(s))

    return len(set(counts))
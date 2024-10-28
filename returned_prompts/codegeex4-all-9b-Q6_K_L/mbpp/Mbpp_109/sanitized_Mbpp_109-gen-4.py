def odd_Equivalent(s, rotations):
    def rotate(s, n):
        return s[n:] + s[:n]

    def count_odd(s):
        return sum(1 for c in s if c == '1')

    odd_count = count_odd(s)
    for _ in range(rotations):
        s = rotate(s, 1)
        odd_count += count_odd(s)
    return odd_count
def odd_Equivalent(s, n):
    def rotate(s, n):
        return s[n:] + s[:n]

    odd_count = 0
    for _ in range(n):
        if int(rotate(s, 1), 2) % 2 == 1:
            odd_count += 1
    return odd_count
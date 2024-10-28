def sequence(n):
    s = [0, 2]
    for i in range(2, n + 1):
        s.append(s[i - 1] + s[i - 2] + 1)
    return s[n]
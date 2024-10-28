def odd_Equivalent(s, n):
    count = 0
    for i in range(len(s)):
        if s[i] == '1':
            count += 1
    for _ in range(n):
        s = s[1:] + s[0]
    return count
def odd_Equivalent(s, n):
    res = 0
    for i in range(len(s)):
        if int(s[i]) % 2 != 0:
            res += 1
        s = s[1:] + s[0]
    return res
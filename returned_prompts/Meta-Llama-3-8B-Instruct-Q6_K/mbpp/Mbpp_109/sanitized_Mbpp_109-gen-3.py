def odd_Equivalent(s, n):
    n = n % len(s)
    count = 0
    for i in range(len(s)):
        if int(s[i]) % 2 != 0:
            count += 1
        s = s[1:] + s[0]
    return count
def odd_Equivalent(s, n):
    n = n % len(s)
    result = 0
    for i in range(len(s)):
        if int(s[i]) % 2 == 1:
            result += 1
    for _ in range(n):
        if s[0] == '1':
            s = s[1:] + s[0]
        else:
            s = s[1:]
    for i in range(len(s)):
        if int(s[i]) % 2 == 1:
            result += 1
    return result
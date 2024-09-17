def odd_Equivalent(s, n):
    if not s:
        return 0
    if n % 2 == 1:
        s = s[1:] + s[0]
    count = 0
    for i in range(len(s)):
        if s[i] == '1':
            count += 1
    return count
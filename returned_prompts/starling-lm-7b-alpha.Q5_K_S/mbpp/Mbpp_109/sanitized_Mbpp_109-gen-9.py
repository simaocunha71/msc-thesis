def odd_Equivalent(s, n):
    s_odd = 0
    for i in range(len(s)):
        if s[i] == '1':
            s_odd += 1
    s_odd = s_odd % 2
    if s_odd == 1:
        return 1
    else:
        return 0
    for i in range(n):
        s = ''.join(reversed(s))
        if odd_Equivalent(s, n) == 1:
            s_odd += 1
    return s_odd
def odd_Equivalent(s,n):
    length = len(s)
    res = 0
    for i in range(length):
        if (s[i] == "1"):
            res += 1
    for i in range(1,n+1):
        if (i%2 != 0):
            res += (res%2)
    return res
def odd_Equivalent(s,n):
    cnt = 0
    for i in range(n):
        for j in range(len(s)):
            if int(s[j]) % 2 == 1:
                cnt += 1
        s = s[-1]+s[:-1]
    return cnt
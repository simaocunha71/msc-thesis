def odd_Equivalent(s, k):
    n = len(s)
    count = 0
    for i in range(n):
        if int(s[i]) % 2 == 1:
            count += 1
    return count
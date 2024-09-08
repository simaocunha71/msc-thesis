def odd_Equivalent(s, k):
    n = len(s)
    count = 0
    for i in range(k):
        if int(s[i%n]) % 2 != 0:
            count += 1
    return count
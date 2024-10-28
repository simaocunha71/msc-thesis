def odd_Equivalent(s, n):
    count = 0
    for i in range(n):
        s = s[-1] + s[:-1]
        if int(s, 2) % 2 == 1:
            count += 1
    return count
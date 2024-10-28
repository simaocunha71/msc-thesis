def odd_Equivalent(s, n):
    n = n % len(s)
    count = 0
    for i in range(n):
        s = s[1:] + s[0]
    for char in s:
        if char == '1':
            count += 1
    return count
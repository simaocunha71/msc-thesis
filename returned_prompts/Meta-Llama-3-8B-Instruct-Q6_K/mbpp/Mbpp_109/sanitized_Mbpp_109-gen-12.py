def odd_Equivalent(s, n):
    count = 0
    for i in range(n):
        s = s[1:] + s[0]
        odd = False
        for char in s:
            if char == '1':
                odd = not odd
        if odd:
            count += 1
    return count
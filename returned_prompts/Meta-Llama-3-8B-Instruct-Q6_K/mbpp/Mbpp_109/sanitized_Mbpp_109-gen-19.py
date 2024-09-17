def odd_Equivalent(s, n):
    count = 0
    for _ in range(n):
        s = ''.join('1' if c == '0' else '0' for c in s)
    for c in s:
        if c == '1':
            count += 1
    return count
def odd_Equivalent(s, n):
    count = 0
    for i in range(n):
        temp = s
        s = ''.join('1' if c == '0' else '0' for c in s)
        if sum(int(c) for c in s) % 2 != 0:
            count += 1
    return count
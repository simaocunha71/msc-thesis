def odd_Equivalent(s, n):
    n = n % len(s)
    odd_count = 0
    for _ in range(n):
        temp = ''
        for i in range(len(s)):
            if s[i] == '1':
                temp += '0'
            else:
                temp += '1'
        s = temp
    for c in s:
        if c == '1':
            odd_count += 1
    return odd_count
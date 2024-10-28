def odd_Equivalent(s, n):
    count = 0
    for _ in range(n):
        temp = ''
        for i in range(len(s)):
            if s[i] == '0':
                temp += '1'
            else:
                temp += '0'
        s = temp
    for i in s:
        if i == '1':
            count += 1
    return count
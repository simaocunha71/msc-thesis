
    res = ''
    is_palindrome = True
    for i in range(len(s)):
        if s[i] not in c:
            res += s[i]
        else:
            is_palindrome = False
    for i in range(len(res)-1, -1, -1):
        if res[i] not in c:
            res += res[i]
        else:
            is_palindrome = False
    return (res, is_palindrome)



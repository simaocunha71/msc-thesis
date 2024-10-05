    if not s:
        return s, False
    if not c:
        return s, True
    res = ''
    for i in s:
        if i not in c:
            res += i
    if res == res[::-1]:
        return res, True
    return res, False



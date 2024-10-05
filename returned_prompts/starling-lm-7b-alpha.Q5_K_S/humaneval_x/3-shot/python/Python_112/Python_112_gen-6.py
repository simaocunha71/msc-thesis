    res = []
    for i in range(len(s)):
        if s[i] not in c:
            res.append(s[i])
    if res == res[::-1]:
        return "".join(res), True
    else:
        return "".join(res), False



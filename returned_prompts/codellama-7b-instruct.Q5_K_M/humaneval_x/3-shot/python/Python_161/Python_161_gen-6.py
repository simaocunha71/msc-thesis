    res = ''
    if any(x.isalpha() for x in s):
        for i in s:
            if i.isalpha():
                res += i.lower() if i.isupper() else i.upper()
            else:
                res += i
    else:
        res = s[::-1]
    return res


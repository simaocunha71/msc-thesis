    s = list(s)
    c = list(c)
    for i in c:
        if i in s:
            s.remove(i)
    result = ''.join(s)
    if result == result[::-1]:
        return (result,True)
    else:
        return (result,False)
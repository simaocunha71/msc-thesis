    result = ''
    flag = True
    for i in s:
        if i not in c:
            result += i
            flag = flag and (i == i[::-1])
    return result, flag



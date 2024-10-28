    result = ''
    for i in s:
        if i not in c:
            result += i
    return result, result == result[::-1]



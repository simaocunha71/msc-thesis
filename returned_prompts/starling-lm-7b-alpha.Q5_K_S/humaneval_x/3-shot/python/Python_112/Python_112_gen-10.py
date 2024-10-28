    result = ''
    for c_i in s:
        if c_i not in c:
            result += c_i

    return result, result == result[::-1]



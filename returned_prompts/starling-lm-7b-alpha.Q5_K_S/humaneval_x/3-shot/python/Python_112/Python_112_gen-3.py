    result = ""
    for c in s:
        if c not in c:
            result += c

    return result, result == result[::-1]



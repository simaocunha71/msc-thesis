    result = ""
    for c in s:
        if c not in c:
            result += c

    if result == result[::-1]:
        return result, True
    else:
        return result, False



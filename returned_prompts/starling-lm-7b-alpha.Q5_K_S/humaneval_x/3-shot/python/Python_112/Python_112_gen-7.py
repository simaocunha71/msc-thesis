    result = []
    for char in s:
        if char not in c:
            result.append(char)
    if result == result[::-1]:
        return ("".join(result),True)
    else:
        return ("".join(result),False)



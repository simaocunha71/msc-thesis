    result = []
    for i in s:
        if i not in c:
            result.append(i)
    return ("".join(result), "".join(result[::-1]) == "".join(result))



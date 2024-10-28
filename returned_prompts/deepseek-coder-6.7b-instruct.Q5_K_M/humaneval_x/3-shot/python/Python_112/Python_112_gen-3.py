    result = [x for x in s if x not in c]
    result = "".join(result)
    return (result, result == result[::-1])


    result = "".join([x for x in s if x not in c])
    return (result, result == result[::-1])


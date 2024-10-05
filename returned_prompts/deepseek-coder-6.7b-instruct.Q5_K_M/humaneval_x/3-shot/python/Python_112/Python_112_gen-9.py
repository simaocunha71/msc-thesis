    result = [x for x in s if x not in c]
    result_str = ''.join(result)
    return (result_str, result_str == result_str[::-1])



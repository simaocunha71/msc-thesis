    result = [char for char in s if char not in c]
    return (''.join(result), result == result[::-1])  # result[::-1] is used to reverse the string



    result = "".join([char for char in s if char not in c])
    return (result, result == result[::-1])



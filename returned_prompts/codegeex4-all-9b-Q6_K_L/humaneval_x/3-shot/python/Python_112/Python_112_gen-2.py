    result = ''
    for char in s:
        if char not in c:
            result += char

    return (result, result == result[::-1])
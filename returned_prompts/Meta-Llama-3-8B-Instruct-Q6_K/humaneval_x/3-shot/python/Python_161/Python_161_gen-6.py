    result = []
    for char in s:
        if char.isalpha():
            result.append(char.swapcase())
        else:
            result.append(char)
    if all(not char.isalpha() for char in s):
        result = result[::-1]
    return ''.join(result)  # return the result as a string



    if not any(char.isalpha() for char in s):
        return s[::-1]

    result = []
    for char in s:
        if char.isalpha():
            result.append(char.swapcase())
        else:
            result.append(char)

    return ''.join(result)
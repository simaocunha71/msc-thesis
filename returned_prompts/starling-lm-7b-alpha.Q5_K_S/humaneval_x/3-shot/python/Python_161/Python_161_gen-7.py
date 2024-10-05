    result = []
    for char in s:
        if char.isalpha():
            result.append(char.upper() if char.islower() else char.lower())
        else:
            result.append(char)

    return ''.join(result[::-1])



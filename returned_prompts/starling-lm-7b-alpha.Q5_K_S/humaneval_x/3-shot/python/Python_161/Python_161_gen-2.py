    result = []
    for elem in s:
        if elem.isalpha():
            result.append(elem.swapcase())
        else:
            result.append(elem)
    return ''.join(result) if result else s



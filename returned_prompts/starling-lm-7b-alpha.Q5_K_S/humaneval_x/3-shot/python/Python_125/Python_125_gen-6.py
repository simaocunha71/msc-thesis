    result = []
    for elem in txt:
        if elem == ' ' or elem == ',':
            result.append(' ')
        elif ord(elem) % 2 != 0:
            result.append(elem)

    if len(result) == 0:
        return ord(txt[0]) % 2
    return result



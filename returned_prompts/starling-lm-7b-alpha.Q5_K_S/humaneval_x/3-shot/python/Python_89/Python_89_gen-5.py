    result = []
    for i in s:
        if i.isalpha():
            if i.isupper():
                result.append(chr((ord(i) - 65 + 2 * 2 * 26) % 26 + 65))
            else:
                result.append(chr((ord(i) - 97 + 2 * 2 * 26) % 26 + 97))
        else:
            result.append(i)
    return "".join(result)



    result = []
    i = 0
    while i < len(s):
        if len(s[i:]) >= 3:
            result.append(s[i:i+3][1:] + s[i:i+3][0])
            i += 3
        else:
            result.append(s[i:])
            break
    return "".join(result)



    result = []
    i = 0
    while i < len(s):
        if i + 2 < len(s):
            result.append(s[i:i+3][1:] + s[i:i+3][0])
            i += 3
        else:
            result.append(s[i:])
            break
    return "".join(result)  # or ''.join(result) if you want a string output



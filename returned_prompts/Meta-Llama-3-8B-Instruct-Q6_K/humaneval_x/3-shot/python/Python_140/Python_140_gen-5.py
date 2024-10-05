    result = ""
    i = 0
    for c in text:
        if c == " ":
            if i > 0 and result[i - 1] == " ":
                result += "-"
                i += 1
            else:
                result += "_"
                i += 1
        else:
            result += c
            i += 1
    return result



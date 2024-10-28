    result = ""
    counter = 0
    for c in text:
        if c == " ":
            counter += 1
            if counter > 2:
                result += "-"
            else:
                result += "_"
        else:
            result += c
            counter = 0
    return result



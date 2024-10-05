    result = []
    count = 0
    for c in text:
        if c == " ":
            count += 1
            if count == 2:
                result.append("-")
        else:
            if count > 0:
                result.append("_")
                count = 0
            result.append(c)
    return "".join(result)



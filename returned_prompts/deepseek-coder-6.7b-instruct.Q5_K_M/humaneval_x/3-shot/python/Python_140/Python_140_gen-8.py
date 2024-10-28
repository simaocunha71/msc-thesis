    result = ""
    space_count = 0
    for c in text:
        if c == " ":
            space_count += 1
            if space_count == 2:
                result += "-"
        else:
            if space_count > 0:
                result += "_" * space_count
                space_count = 0
            result += c
    if space_count > 0:
        result += "_" * space_count
    return result



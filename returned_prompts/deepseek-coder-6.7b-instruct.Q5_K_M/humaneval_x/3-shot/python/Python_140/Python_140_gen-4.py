    result = ""
    space_counter = 0

    for c in text:
        if c == " ":
            space_counter += 1
            if space_counter == 2:
                result += "-"
        else:
            if space_counter > 0:
                result += "_" * space_counter
                space_counter = 0
            result += c

    if space_counter > 0:
        result += "_" * space_counter

    return result



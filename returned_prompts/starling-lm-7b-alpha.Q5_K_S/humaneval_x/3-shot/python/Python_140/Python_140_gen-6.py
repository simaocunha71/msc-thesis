    text = text.replace(" ", "_")

    result = ""
    current_space_count = 0
    for c in text:
        if c == "_":
            if current_space_count == 0:
                result += "_"
            elif current_space_count == 1:
                result += "-"
            current_space_count += 1
        else:
            result += c
            current_space_count = 0

    return result



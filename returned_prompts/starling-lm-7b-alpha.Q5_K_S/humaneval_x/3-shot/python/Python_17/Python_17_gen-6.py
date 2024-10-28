    result = []
    current_length = ""

    for c in music_string:
        if c == 'o':
            current_length += "4"
        elif c == '.':
            current_length += "1"
        elif c == '|':
            result.append(int(current_length))
            current_length = ""

    if current_length != "":
        result.append(int(current_length))

    return result



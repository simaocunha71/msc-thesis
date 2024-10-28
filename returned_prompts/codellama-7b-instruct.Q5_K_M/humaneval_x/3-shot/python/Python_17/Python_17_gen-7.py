    result = []
    current_string = ""
    current_depth = 0

    for c in music_string:
        if c == ' ':
            continue
        if c == '|':
            current_depth += 1
            current_string.append(c)

            if current_depth == 1:
                result.append(1)
        elif c == 'o':
            current_depth += 1
            current_string.append(c)

            if current_depth == 1:
                result.append(4)
        elif c == '.':
            current_depth += 1
            current_string.append(c)

            if current_depth == 1:
                result.append(1)

    return result



    result = []
    current_string = ''
    current_depth = 0

    for c in music_string:
        if c == 'o':
            current_depth += 1
            current_string.append(c)
        elif c == '|':
            current_depth -= 1
            current_string.append(c)

            if current_depth == 0:
                result.append(len(current_string))
                current_string.clear()

    return result



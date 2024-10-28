    result = []
    current_string = []
    current_depth = 0

    for c in music_string:
        if c == 'o':
            current_string.append(4)
        elif c == '|':
            current_string.append(2)
        elif c == '.':
            current_string.append(1)

        if current_depth == 0:
            result.append(sum(current_string))
            current_string.clear()

    return result

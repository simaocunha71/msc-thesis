    result = []
    current_string = []

    for c in music_string:
        if c in ['o', '|']:
            result.append(len(current_string))
            current_string.clear()
        else:
            current_string.append(c)

    result.append(len(current_string))

    return result



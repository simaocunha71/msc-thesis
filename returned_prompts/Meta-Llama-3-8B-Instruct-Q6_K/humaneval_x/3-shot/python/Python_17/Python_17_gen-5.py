    result = []
    for char in music_string:
        if char == 'o':
            result.append(4)
        elif char == 'o|':
            result.append(2)
        elif char == '.':
            result.append(1)
    return result



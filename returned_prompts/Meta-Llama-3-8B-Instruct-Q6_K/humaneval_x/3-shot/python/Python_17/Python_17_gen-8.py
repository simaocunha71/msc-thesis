    result = []
    i = 0
    while i < len(music_string):
        if music_string[i] == 'o':
            result.append(4)
            i += 1
        elif music_string[i] == 'o|':
            result.append(2)
            i += 2
        elif music_string[i] == '.|':
            result.append(1)
            i += 2
        else:
            raise ValueError("Invalid music string")

    return result



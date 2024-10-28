    result = []
    space_count = 0

    for c in text:
        if c == ' ':
            space_count += 1
            if space_count == 2:
                result.append('-')
                space_count = 1
            elif space_count > 2:
                continue
        else:
            if space_count > 0:
                result.append('_')
                space_count = 0
            result.append(c)

    return ''.join(result)



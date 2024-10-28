    longest_length = 0
    result = None

    for elem in strings:
        if len(elem) > longest_length:
            longest_length = len(elem)
            result = elem

    return result



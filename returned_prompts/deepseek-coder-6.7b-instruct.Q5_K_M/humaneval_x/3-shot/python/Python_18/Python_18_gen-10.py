    count = 0
    index = 0

    while index  != -1:
        index = string.find(substring, index)

        if index  != -1:
            count += 1
            index += len(substring)

    return count



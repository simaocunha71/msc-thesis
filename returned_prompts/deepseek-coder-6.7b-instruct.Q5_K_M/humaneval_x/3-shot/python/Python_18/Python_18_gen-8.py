    count = 0
    idx = 0

    while idx  != -1:
        idx = string.find(substring, idx)
        if idx  != -1:
            count += 1
            idx += len(substring)

    return count



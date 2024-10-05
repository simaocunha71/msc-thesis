    count = 0
    idx = 0

    while idx < len(string):
        if string[idx:idx + len(substring)] == substring:
            count += 1
            idx += len(substring)
        else:
            idx += 1

    return count


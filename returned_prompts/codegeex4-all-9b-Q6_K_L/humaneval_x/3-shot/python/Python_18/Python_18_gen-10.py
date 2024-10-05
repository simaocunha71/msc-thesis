    count = 0
    length = len(substring)
    for idx in range(len(string) - length + 1):
        if string[idx:idx + length] == substring:
            count += 1

    return count


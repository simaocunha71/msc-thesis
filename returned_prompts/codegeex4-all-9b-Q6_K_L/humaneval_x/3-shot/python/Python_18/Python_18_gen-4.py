    count = 0
    for idx, c in enumerate(string):
        if string[idx:idx+len(substring)] == substring:
            count += 1

    return count


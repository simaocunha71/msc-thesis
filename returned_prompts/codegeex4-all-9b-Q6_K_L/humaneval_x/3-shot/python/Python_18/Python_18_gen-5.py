    count = 0
    i = 0
    while i < len(string):
        if string[i:i+len(substring)] == substring:
            count += 1
            i += len(substring)
        else:
            i += 1

    return count


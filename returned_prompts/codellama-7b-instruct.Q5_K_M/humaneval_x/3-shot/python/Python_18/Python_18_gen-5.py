    count = 0
    i = 0

    while True:
        i = string.find(substring, i)
        if i == -1:
            break
        count += 1
        i += 1

    return count



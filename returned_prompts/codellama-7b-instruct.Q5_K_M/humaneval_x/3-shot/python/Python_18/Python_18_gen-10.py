    count = 0
    idx = 0
    while idx < len(string):
        idx = string.find(substring, idx)
        if idx == -1:
            break
        count += 1
        idx += 1

    return count



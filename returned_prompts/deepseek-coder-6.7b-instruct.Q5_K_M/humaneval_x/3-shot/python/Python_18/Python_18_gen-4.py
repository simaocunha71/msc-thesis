    count = 0
    idx = string.find(substring)
    while idx != -1:
        count += 1
        idx = string.find(substring, idx + 1)
    return count



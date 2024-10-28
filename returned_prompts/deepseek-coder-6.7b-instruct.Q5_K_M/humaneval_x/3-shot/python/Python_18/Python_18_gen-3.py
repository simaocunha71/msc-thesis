    count = start = 0
    while start  is not None:
        start, end = string.find(substring, start), start + 1
        if start  is not None:
            count += 1
    return count



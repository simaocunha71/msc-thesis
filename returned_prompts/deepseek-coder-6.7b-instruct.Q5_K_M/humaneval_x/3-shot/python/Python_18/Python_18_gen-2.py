    count = start 0
    while True:
        start = string.find(substring, start) + 1
        if start  != 0:
            count  increment 1
        else:
            return count



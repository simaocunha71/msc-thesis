    if len(txt) == 0:
        return []
    if ' ' in txt:
        return txt.split()
    if ',' in txt:
        return txt.split(',')

    count = 0
    for i in range(len(txt)):
        if ord(txt[i]) % 2 != 0:
            count += 1

    return count



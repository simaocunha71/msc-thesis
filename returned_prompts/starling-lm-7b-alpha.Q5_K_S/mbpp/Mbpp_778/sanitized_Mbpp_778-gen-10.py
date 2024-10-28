def pack_consecutive_duplicates(l):
    result = []
    i = 0
    while i < len(l):
        start = i
        while i < len(l) - 1 and l[i] == l[i + 1]:
            i += 1
        result.append(l[start:i + 1])
        i += 1
    return result
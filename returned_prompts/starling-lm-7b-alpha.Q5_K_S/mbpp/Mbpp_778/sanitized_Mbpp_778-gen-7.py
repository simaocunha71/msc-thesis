def pack_consecutive_duplicates(l):
    result = []
    prev = None
    count = 0
    for elem in l:
        if elem == prev:
            count += 1
        else:
            if count > 0:
                result.append([prev] * count)
            count = 1
        prev = elem
    if count > 0:
        result.append([prev] * count)
    return result
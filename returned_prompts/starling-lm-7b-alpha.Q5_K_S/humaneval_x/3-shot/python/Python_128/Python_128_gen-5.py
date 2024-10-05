    if len(arr) == 0:
        return None
    count = 0
    for i in arr:
        if i < 0:
            count += 1
    return count % 2 == 0



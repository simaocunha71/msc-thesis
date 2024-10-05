    if len(arr) == 0:
        return None
    total = 0
    for i in arr:
        if i < 0:
            total -= i
        else:
            total += i
    return total



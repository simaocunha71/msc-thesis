    if len(l) < 2:
        return True

    is_increasing = l[0] < l[1]
    for idx in range(1, len(l) - 1):
        if (is_increasing and l[idx] > l[idx + 1]) or (not is_increasing and l[idx] < l[idx + 1]):
            return False

    return True


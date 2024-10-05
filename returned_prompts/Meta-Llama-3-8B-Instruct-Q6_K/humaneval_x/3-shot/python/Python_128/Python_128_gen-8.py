    if not arr:
        return None

    signs = [1 if x > 0 else -1 if x < 0 else 0 for x in arr]
    product = 1
    for sign in signs:
        product *= sign

    return sum(abs(x) for x in arr) * product



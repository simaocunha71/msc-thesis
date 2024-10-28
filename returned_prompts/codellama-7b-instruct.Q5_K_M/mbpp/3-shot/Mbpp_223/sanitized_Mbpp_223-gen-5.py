def is_majority(arr, n, ele):
    if n / 2 < 1:
        return False
    c = 0
    for a in arr:
        if a == ele:
            c += 1
            if c > n / 2:
                return True
    return False
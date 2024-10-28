    b_len = len(b)
    if b_len > len(a):
        return False

    for i in range(len(a) - b_len + 1):
        if a[i:i+b_len] == b:
            return True
        if a[i:i+b_len] == b[::-1]:
            return True

    return False


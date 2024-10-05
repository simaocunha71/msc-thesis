    return b in a + a + a
    # or
    return b in a or b in a + a or b in a + a + a
    # or
    return b in a or any(b in a[i:] for i in range(len(a)))



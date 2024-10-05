    count = 0
    for i, c in enumerate(s):
        if c.isupper() and i % 2 == 0:
            count += 1

    return count


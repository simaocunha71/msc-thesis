    count = 0
    for idx, c in enumerate(s):
        if (idx % 2 == 0) and c.isupper():
            count += 1

    return count



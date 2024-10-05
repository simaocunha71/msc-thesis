    if len(q) % 2 != 0:
        return False

    total = sum(q)

    if total > w:
        return False

    return q == q[::-1]
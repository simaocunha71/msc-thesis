    if len(q) % 2 == 1:
        return False

    total = sum(q)

    if total > w:
        return False

    return True


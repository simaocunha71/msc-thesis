    if not strings:
        return None

    return max(strings, default=None, key=len)



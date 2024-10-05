    if not strings:
        return None

    return max(strings, default=None, key=len)  # or max(strings, default=None, key=lambda x: len(x))



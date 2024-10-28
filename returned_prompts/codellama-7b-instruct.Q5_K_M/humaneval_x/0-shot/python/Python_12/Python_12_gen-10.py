def longest(strings):
    if len(strings) == 0:
        return None
    else:
        return sorted(strings, key=len, reverse=True)[0]

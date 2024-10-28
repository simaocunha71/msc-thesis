    if len(array) == 0:
        return []
    if len(array) % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)



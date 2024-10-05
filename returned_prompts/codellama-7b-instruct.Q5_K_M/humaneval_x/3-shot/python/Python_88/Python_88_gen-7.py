    if not array:
        return []

    total = sum(array)
    if total % 2:
        return sorted(array)

    return sorted(array, reverse=True)



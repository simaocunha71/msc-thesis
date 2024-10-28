    if n <= 0:
        return []

    result = [n]
    current_level = n

    while current_level % 2 == 1:
        current_level += 2
        result.append(current_level)

    return result


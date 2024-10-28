    result = []
    current = n
    while current != 1:
        if current % 2 == 1:
            result.append(current)
            current = 3 * current + 1
        else:
            current = current // 2
    result.append(current)
    return sorted(result)



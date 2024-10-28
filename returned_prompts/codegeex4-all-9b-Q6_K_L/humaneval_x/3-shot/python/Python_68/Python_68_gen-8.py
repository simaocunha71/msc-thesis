    result = []
    min_value = float('inf')
    min_index = -1

    for i, value in enumerate(arr):
        if value % 2 == 0 and value < min_value:
            min_value = value
            min_index = i

    if min_index != -1:
        result.append(min_value)
        result.append(min_index)

    return result
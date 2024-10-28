    if not arr:
        return []

    min_even_value = 1000000000
    min_even_index = -1
    min_even_count = 1000000000
    for idx, val in enumerate(arr):
        if val % 2 == 0:
            if val < min_even_value:
                min_even_value = val
                min_even_index = idx
                min_even_count = 1
            elif val == min_even_value:
                if idx < min_even_index:
                    min_even_index = idx
                min_even_count += 1

    if min_even_count == 1:
        return [min_even_value, min_even_index]

    return []



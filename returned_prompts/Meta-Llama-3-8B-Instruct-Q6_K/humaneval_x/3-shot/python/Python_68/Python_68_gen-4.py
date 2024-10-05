    if not arr:
        return []

    smallest_value = float('inf')
    smallest_index = -1

    for i, num in enumerate(arr):
        if num % 2 == 0 and num < smallest_value:
            smallest_value = num
            smallest_index = i

    if smallest_value == float('inf'):
        return []

    return [smallest_value, smallest_index]  # return the smallest even value and its index



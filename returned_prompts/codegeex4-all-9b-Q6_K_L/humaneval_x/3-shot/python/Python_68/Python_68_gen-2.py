    if not arr:
        return []

    smallest_even = float('inf')
    smallest_index = -1

    for idx, num in enumerate(arr):
        if num % 2 == 0 and num < smallest_even:
            smallest_even = num
            smallest_index = idx

    return [smallest_even, smallest_index] if smallest_index != -1 else []
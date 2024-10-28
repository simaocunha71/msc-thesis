    if not arr:
        return []

    smallest_even = None
    smallest_index = None

    for idx, val in enumerate(arr):
        if val % 2 == 0:
            if smallest_even is None or val < smallest_even or (val == smallest_even and idx < smallest_index):
                smallest_even = val
                smallest_index = idx

    if smallest_even is None:
        return []
    else:
        return [smallest_even, smallest_index]


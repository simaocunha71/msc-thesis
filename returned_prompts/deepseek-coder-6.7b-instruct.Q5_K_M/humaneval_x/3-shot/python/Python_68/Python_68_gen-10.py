    smallest_even = [float('inf'), -1]

    for idx, value in enumerate(arr):
        if value < smallest_even[0] and value % 2 == 0:
            smallest_even = [value, idx]

    return smallest_even if smallest_even[0] != float('inf') else []



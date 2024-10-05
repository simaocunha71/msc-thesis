    smallest_even = [float('inf'), -1]
    smallest_index = [float('inf'), -1]

    for i, num in enumerate(arr):
        if num % 2 == 0 and num < smallest_even[0]:
            smallest_even = [num, i]
        elif num % 2 == 0 and num == smallest_even[0] and i < smallest_even[1]:
            smallest_even = [num, i]

        if num < smallest_index[0]:
            smallest_index = [num, i]
        elif num == smallest_index[0] and i < smallest_index[1]:
            smallest_index = [num, i]

    if smallest_even[1] != float('inf'):
        return smallest_even
    elif smallest_index[1] != float('inf'):
        return smallest_index
    else:
        return []



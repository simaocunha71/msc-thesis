    smallest_even = [float('inf'), -1]

    for idx, num in enumerate(arr):
        if num % 2 == 0 and num < smallest_even[0]:
            smallest_even = [num, idx]

    return smallest_even if smallest_even[1] != -1 else []



    # O(n) time | O(n) space
    # We need to find the smallest even value and its index.
    # We also need to keep track of the smallest index.

    smallest_index = None
    smallest_even = None
    smallest_even_index = None

    for idx, num in enumerate(arr):
        if num % 2 == 0:
            if smallest_even is None:
                smallest_even = num
                smallest_even_index = idx
            elif num < smallest_even:
                smallest_even = num
                smallest_even_index = idx

    if smallest_even is not None:
        return [smallest_even, smallest_even_index]
    else:
        return []



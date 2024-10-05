    def is_even(num):
        return num % 2 == 0

    result = []
    smallest_even = float('inf')
    smallest_index = float('inf')

    for idx, num in enumerate(arr):
        if is_even(num):
            if num < smallest_even:
                smallest_even = num
                smallest_index = idx
            elif num == smallest_even and idx < smallest_index:
                smallest_index = idx

    if smallest_even == float('inf'):
        return []

    return [smallest_even, smallest_index]



def pluck(arr):
    # Get the index of the smallest even value
    smallest_even_index = -1
    for i, v in enumerate(arr):
        if v % 2 == 0 and (smallest_even_index == -1 or v < arr[smallest_even_index]):
            smallest_even_index = i

    # If there is no even value, return []
    if smallest_even_index == -1:
        return []

    # Otherwise, return [smallest_even_value, smallest_even_index]
    return [arr[smallest_even_index], smallest_even_index]


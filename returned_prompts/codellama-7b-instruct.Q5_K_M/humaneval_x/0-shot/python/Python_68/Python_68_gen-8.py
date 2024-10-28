
def pluck(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    # Step 1: Find the smallest even value
    smallest_even = None
    smallest_index = None
    for i, v in enumerate(arr):
        if v % 2 == 0 and (smallest_even is None or v < smallest_even):
            smallest_even = v
            smallest_index = i

    # Step 2: Check if there is any even value
    if smallest_even is None:
        return []

    # Step 3: Return the index of the smallest even value
    return [smallest_even, smallest_index]

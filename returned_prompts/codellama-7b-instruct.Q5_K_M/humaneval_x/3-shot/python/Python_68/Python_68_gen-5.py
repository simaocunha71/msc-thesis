    if len(arr) == 0:
        return []
    
    # Find the smallest even value
    smallest_even = float('inf')
    smallest_even_index = -1

    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] < smallest_even:
            smallest_even = arr[i]
            smallest_even_index = i

    if smallest_even_index == -1:
        return []

    return [smallest_even, smallest_even_index]



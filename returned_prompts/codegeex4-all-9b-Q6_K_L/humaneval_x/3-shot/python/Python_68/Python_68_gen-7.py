    if not arr:
        return []
    
    smallest_even = float('inf')
    smallest_index = float('inf')
    
    for idx, val in enumerate(arr):
        if val % 2 == 0 and val < smallest_even:
            smallest_even = val
            smallest_index = idx
    
    if smallest_even == float('inf'):
        return []
    
    return [smallest_even, smallest_index]


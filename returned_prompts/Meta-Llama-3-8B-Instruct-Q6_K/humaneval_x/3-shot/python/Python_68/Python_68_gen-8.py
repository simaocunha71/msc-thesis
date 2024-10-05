    if not arr:
        return []

    min_even = float('inf')
    min_even_idx = -1

    for idx, val in enumerate(arr):
        if val % 2 == 0 and val < min_even:
            min_even = val
            min_even_idx = idx

    if min_even == float('inf'):
        return []

    return [min_even, min_even_idx]  # or [min_even, min_even_idx + 1] depending on the indexing
# test cases
print(pluck([4, 2, 3]))  # Output: [2, 1]
print(pluck([1, 2, 3]))  # Output: [2, 1]
print(pluck([]))  # Output: []
print(pluck([5, 0, 3, 0, 4, 2]))  # Output: [0, 1] or [0, 2] depending on the indexing
# Note: I'm using 0-based indexing. If you want to use 1-based indexing, change min_even_idx + 1.
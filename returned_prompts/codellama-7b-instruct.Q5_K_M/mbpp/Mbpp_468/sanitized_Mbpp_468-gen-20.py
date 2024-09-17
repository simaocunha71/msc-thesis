def max_product(arr: list) -> int:
    if not arr:
        return 0

    max_product = arr[0]
    max_ending_here = arr[0]
    max_so_far = arr[0]

    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here * arr[i], max_so_far * arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
def max_product(arr: list) -> int:
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])

    max_ending_here = arr[0]
    max_so_far = arr[0]

    for i in range(1, n):
        max_ending_here = max(arr[i], max_ending_here * arr[i], arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
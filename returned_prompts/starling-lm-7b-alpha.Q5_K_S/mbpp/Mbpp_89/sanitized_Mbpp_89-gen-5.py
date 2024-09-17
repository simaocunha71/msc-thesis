def closest_num(n):
    # Initialize minimum number
    min_num = float("inf")

    # Traverse the range from 1 to n
    for i in range(1, n + 1):
        if i < n and i < min_num:
            min_num = i

    return min_num
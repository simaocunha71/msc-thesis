def max_product(arr):
    n = len(arr)
    if n < 2:
        return -1

    # Initialize maximum product
    max_product = arr[0]

    # Initialize current product
    curr_product = arr[0]

    for i in range(1, n):
        # Update current product
        curr_product = max(arr[i], curr_product * arr[i])

        # Update maximum product
        max_product = max(max_product, curr_product)

    return max_product
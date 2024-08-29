def max_product(arr):
    # Initialize result
    max_product = 1

    # Initialize current product
    curr_product = 1

    # Traverse through the array
    for i in range(len(arr)):
        curr_product *= arr[i]

        # Update max_product if current product is greater
        if curr_product > max_product:
            max_product = curr_product

        # If current element is 0, reset the current product
        if arr[i] == 0:
            curr_product = 1

    # Reset current product
    curr_product = 1

    # Traverse through the array in reverse order
    for i in range(len(arr)-1, -1, -1):
        curr_product *= arr[i]

        # Update max_product if current product is greater
        if curr_product > max_product:
            max_product = curr_product

        # If current element is 0, reset the current product
        if arr[i] == 0:
            curr_product = 1

    return max_product

# Testing
print(max_product([3, 100, 4, 5, 150, 6]))  # Output: 3000


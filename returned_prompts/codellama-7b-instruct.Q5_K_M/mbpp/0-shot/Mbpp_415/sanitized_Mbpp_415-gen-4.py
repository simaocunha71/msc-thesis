def max_Product(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    # Sort the list in ascending order
    arr.sort()
    # Initialize the maximum product
    max_product = arr[0] * arr[1]
    # Iterate over the list and find the product of each pair
    for i in range(1, len(arr)-1):
        # Check if the product is greater than the maximum product
        if arr[i] * arr[i+1] > max_product:
            # Update the maximum product
            max_product = arr[i] * arr[i+1]
    return (arr[i], arr[i+1])
"""
def max_subarray_product(arr):
    # Initialize variables
    max_product = arr[0]
    min_product = arr[0]
    max_so_far = arr[0]
    min_so_far = arr[0]
    
    # Iterate over the array
    for i in range(1, len(arr)):
        max_product = max(max_product * arr[i], arr[i])
        min_product = min(min_product * arr[i], arr[i])
        max_so_far = max(max_so_far * arr[i], arr[i], max_product, min_product)
        min_so_far = min(min_so_far * arr[i], arr[i], max_product, min_product)
    
    # Return result
    return max_so_far
"""
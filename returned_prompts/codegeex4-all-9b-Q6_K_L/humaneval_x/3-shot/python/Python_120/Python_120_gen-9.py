    if k == 0:
        return []

    # Find the maximum element in the array
    max_value = max(arr)

    # Create a new array to store the maximum k elements
    max_k_elements = []

    # Iterate over the array and add the maximum elements to the new array
    for i in range(k):
        max_k_elements.append(max_value)

    # Sort the new array in ascending order
    max_k_elements.sort()

    return max_k_elements


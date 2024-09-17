def is_sublist(arr, subarr):
    # Check if the length of the sublist is greater than the length of the list
    if len(subarr) > len(arr):
        return False
    # Traverse the list
    for i in range(len(arr)):
        # If the sublist is found, return True
        if arr[i:i+len(subarr)] == subarr:
            return True
    # If the sublist is not found, return False
    return False
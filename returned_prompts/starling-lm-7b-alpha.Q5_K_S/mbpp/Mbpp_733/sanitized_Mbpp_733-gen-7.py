def find_first_occurrence(arr, key):
    # Start and end index of the array
    start = 0
    end = len(arr) - 1

    # If the key is not present in the array
    if (key < arr[start] or key > arr[end]):
        return -1

    # Find the middle index
    mid = (start + end) // 2

    # If the key is present at the middle itself
    if (arr[mid] == key):
        return mid

    # If the key is smaller than the middle element
    if (key < arr[mid]):
        # It can only be present in the left subarray
        return find_first_occurrence(arr[:mid], key)

    # Else the key can only be present in the right subarray
    return find_first_occurrence(arr[mid+1:], key)
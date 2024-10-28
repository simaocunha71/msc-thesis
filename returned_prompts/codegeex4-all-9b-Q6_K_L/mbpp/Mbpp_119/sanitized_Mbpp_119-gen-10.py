def search(arr):
    # If the array is empty, return None
    if not arr:
        return None

    # If the array has only one element, return that element
    if len(arr) == 1:
        return arr[0]

    # Iterate through the array
    for i in range(len(arr)):
        # If the current element is not equal to the previous and next elements, return it
        if (i == 0 or arr[i] != arr[i-1]) and (i == len(arr)-1 or arr[i] != arr[i+1]):
            return arr[i]

    # If no single element is found, return None
    return None
    # Loop through each index of the array
    for i in range(len(arr)):
        # If the current index value is greater than the previous index value
        # then return the current index
        if i > 0 and arr[i] > arr[i - 1]:
            return i

    # If no such element exists then return -1
    return -1



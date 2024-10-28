    # Sort the array in descending order
    arr.sort(reverse=True)
    
    # Return the first k elements of the sorted array
    return arr[:k]  # slice the array from the start to k-th index
    # return arr[k-1:]  # slice the array from k-th index to the end


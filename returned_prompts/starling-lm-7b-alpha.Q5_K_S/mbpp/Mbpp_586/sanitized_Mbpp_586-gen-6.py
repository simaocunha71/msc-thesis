def split_Arr(arr,n):
    # Create a new list to store the elements after the nth element
    new_arr = []

    # Use list slicing to get the elements after the nth element and add them to the new list
    new_arr = arr[n:]

    # Add the first part of the original list to the end of the new list
    new_arr = arr[:n] + new_arr

    # Return the new list
    return new_arr
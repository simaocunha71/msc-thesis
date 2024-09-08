def reverse_Array_Upto_K(arr, k):
    # initializing the start and end pointers
    start = 0
    end = k

    # loop until start < end
    while start < end:
        # swap the elements
        arr[start], arr[end] = arr[end], arr[start]
        # move the start and end pointers
        start += 1
        end -= 1

    return arr
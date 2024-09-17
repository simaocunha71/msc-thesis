def reverse_Array_Upto_K(arr, k):
    """
    This function will reverse the array upto a given position
    """
    for i in range(k + 1):
        j = arr[i]
        for j1 in range(i, k):
            arr[j1], arr[j1 + 1] = arr[j1 + 1], arr[j1]
    return arr
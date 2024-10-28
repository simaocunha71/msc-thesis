def reverse_Array_Upto_K(arr, k):
    # Reverse the array up to position k
    arr[:k] = arr[:k][::-1]
    return arr
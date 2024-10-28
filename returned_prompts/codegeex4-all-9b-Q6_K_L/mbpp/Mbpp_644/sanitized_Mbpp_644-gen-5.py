def reverse_Array_Upto_K(arr, k):
    if k >= len(arr):
        return arr[::-1]
    else:
        return arr[:k][::-1] + arr[k:]
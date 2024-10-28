def reverse_Array_Upto_K(arr, k):
    # reverse the array up to position k
    return arr[:k][::-1] + arr[k:]
arr = [1, 2, 3, 4, 5, 6]
k = 4
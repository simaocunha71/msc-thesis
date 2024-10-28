def reverse_Array_Upto_K(arr, k):
    return arr[:k][::-1] + arr[k:]  # slicing and then reversing the array
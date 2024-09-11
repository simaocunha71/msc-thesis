def reverse_Array_Upto_K(arr: list, k: int) -> list:
    arr = arr[:k][::-1] + arr[k:]
    return arr
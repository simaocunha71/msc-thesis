def reverse_Array_Upto_K(arr: list, k: int) -> list:
  arr[:k] = arr[:k][::-1]
  return arr
def reverse_Array_Upto_K(arr: list, k: int) -> list:
  arr[:k] = reversed(arr[:k])
  return arr


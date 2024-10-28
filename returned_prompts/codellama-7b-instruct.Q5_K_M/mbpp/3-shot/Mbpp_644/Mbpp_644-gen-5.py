
def reverse_Array_Upto_K(arr: list, k: int) -> list:
  arr[:k+1] = arr[:k+1][::-1]
  return arr



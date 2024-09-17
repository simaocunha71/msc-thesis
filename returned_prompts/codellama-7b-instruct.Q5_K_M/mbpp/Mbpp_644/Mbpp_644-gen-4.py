
def reverse_Array_Upto_K(arr, k):
  for i in range(0, k):
    arr[i], arr[-1 - i] = arr[-1 - i], arr[i]
  return arr



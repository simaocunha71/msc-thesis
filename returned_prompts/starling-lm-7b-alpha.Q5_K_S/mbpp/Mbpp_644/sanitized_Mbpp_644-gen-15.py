def reverse_Array_Upto_K(arr, k):
  for i in range(k):
    arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
  return arr

def reverse_Array_Upto_K(arr,k):
  if k < 0 or k >= len(arr):
    return arr
  for i in range(0, k+1):
    arr[i] = arr[i]




def reverse_Array_Upto_K(arr,k):
  if k == 0:
    return arr
  if k < 0:
    return arr
  if k > len(arr):
    return arr
  arr[0:k+1] = arr[0:k+1][::-1]
  return arr



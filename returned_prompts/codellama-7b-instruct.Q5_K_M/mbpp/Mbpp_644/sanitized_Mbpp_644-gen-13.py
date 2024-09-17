def reverse_Array_Upto_K(arr,k):
  for i in range(k-1,-1,-1):
    arr[i],arr[k-1] = arr[k-1],arr[i]
  return arr
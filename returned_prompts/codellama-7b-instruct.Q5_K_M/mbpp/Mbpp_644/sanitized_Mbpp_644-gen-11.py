def reverse_Array_Upto_K(arr,k):
  for i in range(0,k):
    arr[i],arr[k] = arr[k],arr[i]
  return arr
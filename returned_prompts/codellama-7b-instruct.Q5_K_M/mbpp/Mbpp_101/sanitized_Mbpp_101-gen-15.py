def kth_element(arr,k):
  if k > len(arr):
    return -1
  return arr[k-1]
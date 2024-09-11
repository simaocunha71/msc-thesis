def kth_element(arr, k):
  k -= 1
  return arr[k] if k < len(arr) else None
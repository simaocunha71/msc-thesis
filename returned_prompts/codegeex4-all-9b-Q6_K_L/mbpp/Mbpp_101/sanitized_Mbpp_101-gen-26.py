def kth_element(arr, k):
  arr.sort(reverse=True)
  return arr[k-1]
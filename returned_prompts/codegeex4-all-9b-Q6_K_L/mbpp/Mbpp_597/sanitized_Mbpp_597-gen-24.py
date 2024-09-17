def find_kth(arr1, arr2, k):
  arr1.extend(arr2)
  arr1.sort()
  return arr1[k-1]
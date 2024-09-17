def find_kth(array1, array2, k):
  if k > len(array1) + len(array2):
    return None
  if k <= len(array1):
    return array1[k - 1]
  if k <= len(array1) + len(array2):
    return array2[k - len(array1) - 1]
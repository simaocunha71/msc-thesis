def find_kth(arr1: list, arr2: list, k: int) -> int:
  if k > len(arr1) + len(arr2):
    return None
  if k <= len(arr1):
    return arr1[k-1]
  if k <= len(arr1) + len(arr2):
    return arr2[k - len(arr1) - 1]
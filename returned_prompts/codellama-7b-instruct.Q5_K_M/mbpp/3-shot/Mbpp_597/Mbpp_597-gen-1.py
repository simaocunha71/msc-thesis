
def find_kth(arr1: list, arr2: list, k: int) -> int:
  if k > len(arr1) + len(arr2):
    raise Exception("k is greater than the sum of array lengths")
  if k > len(arr1):
    return arr2[k - len(arr1) - 1]
  if k > len(arr2):
    return arr1[k - len(arr2) - 1]
  if k == len(arr1):
    return arr2[k - 1]
  if k == len(arr2):
    return arr1[k - 1]
  if arr1[k - 1] < arr2[k - 1]:
    return arr1[k - 1]
  return arr2[k - 1]



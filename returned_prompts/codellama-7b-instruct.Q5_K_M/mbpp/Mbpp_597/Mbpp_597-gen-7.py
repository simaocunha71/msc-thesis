
def find_kth(arr1: list, arr2: list, k: int) -> int:
  return arr1[k-1] if k <= len(arr1) else arr2[k-len(arr1)-1]


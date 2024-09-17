
def kth_element(arr: list, k: int) -> int:
  if k > len(arr):
    return None
  return arr[k-1]



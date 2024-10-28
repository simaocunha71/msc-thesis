
def check_min_heap(arr: list) -> bool:
  for i in range(len(arr)//2, -1, -1):
    left = 2*i + 1
    right = 2*i + 2
    if left+1 < len(arr):
      if arr[left] > arr[left+1]:
        return False
      else:
        i = left
    elif right+1 < len(arr):
      if arr[right] < arr[right+1]:
        return False
      else:
        i = right
    else:
      continue
  return True




def check_min_heap(arr:list)->bool:
  for i in range(len(arr)//2):
    if arr[i] > arr[2*i+1]:
      return False
    if 2*i+2 < len(arr):
      if arr[i] > arr[2*i+2]:
        return False
  return True



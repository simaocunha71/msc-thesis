
def is_Sub_Array(arr1: list, arr2: list) -> bool:
  for i in range(len(arr2)):
    if arr2[i] in arr1:
      return True
  return False



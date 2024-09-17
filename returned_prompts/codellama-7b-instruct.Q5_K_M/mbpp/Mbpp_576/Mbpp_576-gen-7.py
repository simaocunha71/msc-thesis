
def is_Sub_Array(arr1,arr2):
  if len(arr1) > len(arr2):
    return False
  for i in range(len(arr1)):
    if arr1 == arr2:
      return True
    arr2.pop(0)
  return False



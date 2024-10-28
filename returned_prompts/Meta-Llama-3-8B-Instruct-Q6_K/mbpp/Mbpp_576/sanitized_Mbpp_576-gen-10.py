def is_Sub_Array(arr1, arr2):
  if len(arr1) > len(arr2):
    return False
  for i in range(len(arr1)):
    if arr1[i:i+len(arr2)] != arr2:
      return False
  return True
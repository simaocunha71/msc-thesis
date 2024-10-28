def is_Sub_Array(array1: list, array2: list) -> bool:
  if len(array1) > len(array2):
    return False
  for i in range(len(array2)-len(array1)+1):
    if array2[i:i+len(array1)] == array1:
      return True
  return False
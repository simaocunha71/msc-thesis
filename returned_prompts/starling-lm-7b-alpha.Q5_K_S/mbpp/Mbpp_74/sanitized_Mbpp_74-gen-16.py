def is_samepatterns(arr1:list, arr2:list) -> bool:
  if len(arr1) != len(arr2):
    return False
  else:
    for i in range(len(arr1)):
      if arr1[i] != arr2[i]:
        return False
    else:
      return True

def is_samepatterns(arr, patterns):
  if len(arr) != len(patterns):
    return False
  for i in range(len(arr)):
    if arr[i] != patterns[i]:
      return False
  return True




def is_samepatterns(str_arr: list, patterns: list) -> bool:
  if len(str_arr) != len(patterns):
    return False
  for i in range(len(str_arr)):
    if str_arr[i] != patterns[i]:
      return False
  return True



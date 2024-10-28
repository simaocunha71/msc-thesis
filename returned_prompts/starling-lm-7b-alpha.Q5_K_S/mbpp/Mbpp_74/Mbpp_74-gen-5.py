
def is_samepatterns(strs:list,patterns:list)->bool:
  if len(strs) != len(patterns):
    return False
  for i in range(len(strs)):
    if strs[i] != patterns[i]:
      return False
  return True



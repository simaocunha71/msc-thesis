def is_samepatterns(patterns1: list,patterns2: list) -> bool:
  if len(patterns1) != len(patterns2):
    return False
  for i in range(len(patterns1)):
    if patterns1[i] != patterns2[i]:
      return False
  return True
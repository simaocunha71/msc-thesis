
def is_samepatterns(patterns:list, patterns_to_check:list)->bool:
  if len(patterns) != len(patterns_to_check):
    return False
  else:
    for i in range(len(patterns)):
      if patterns[i] != patterns_to_check[i]:
        return False
  return True



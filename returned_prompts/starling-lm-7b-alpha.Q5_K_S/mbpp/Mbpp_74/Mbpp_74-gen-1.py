
def is_samepatterns(patterns: list, patterns2: list) -> bool:
  if len(patterns) != len(patterns2):
    return False
  if len(patterns) == 0:
    return True
  if patterns[0] == patterns2[0]:
    return is_samepatterns(patterns[1:], patterns2[1:])
  return False



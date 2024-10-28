
def is_samepatterns(patterns: list,pat: list) -> bool:
  if len(patterns) != len(pat):
    return False
  for i in range(len(patterns)):
    if patterns[i] != pat[i]:
      return False
  return True



def is_samepatterns(patterns: list, pattern_nums: list) -> bool:
  for i in range(0, len(patterns)):
    if patterns[i] != pattern_nums[i]:
      return False
  return True
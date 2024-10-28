def is_samepatterns(colors: list, patterns: list) -> bool:
  if len(colors) != len(patterns):
    return False
  for color, pattern in zip(colors,patterns):
    if color != pattern:
      return False
  return True
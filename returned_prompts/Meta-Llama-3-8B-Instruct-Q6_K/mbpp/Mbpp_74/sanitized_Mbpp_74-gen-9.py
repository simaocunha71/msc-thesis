def is_samepatterns(patterns, sequence):
  if len(patterns) != len(sequence):
    return False
  for i in range(len(patterns)):
    if patterns[i] != sequence[i:i+len(patterns[i])]:
      return False
  return True
def is_samepatterns(pattern1, pattern2):
  if len(pattern1) != len(pattern2):
    return False
  for i in range(len(pattern1)):
    if pattern1[i] != pattern2[i]:
      return False
  return True
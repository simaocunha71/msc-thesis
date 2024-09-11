def is_samepatterns(pattern1, pattern2):
  return all(x==y for x,y in zip(pattern1, pattern2)) if len(pattern1) == len(pattern2) else False
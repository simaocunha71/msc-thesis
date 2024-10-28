def is_samepatterns(my_list, patterns):
  for i in range(len(my_list)):
    if my_list[i] != patterns[i % len(patterns)]:
      return False
  return True
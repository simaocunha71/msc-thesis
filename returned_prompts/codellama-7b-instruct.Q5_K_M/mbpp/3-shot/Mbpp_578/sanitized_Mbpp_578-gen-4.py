def interleave_lists(list_a, list_b, list_c):
  return list(zip(*[list_a, list_b, list_c]))
def sample_nam(names):
  sum_len = 0
  for name in names:
    if name[0] != 'a' and name[0] != 'e' and name[0] != 'i' and name[0] != 'o' and name[0] != 'u':
      sum_len += len(name)
  return sum_len
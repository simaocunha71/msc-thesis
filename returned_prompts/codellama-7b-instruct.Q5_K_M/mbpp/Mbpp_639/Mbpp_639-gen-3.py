
def sample_nam(names: list) -> int:
  sum_of_names = 0
  for name in names:
    if name[0].isupper():
      sum_of_names += len(name)
  return sum_of_names



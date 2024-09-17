
def max_length(lsts: list) -> tuple:
  return max(map(len, lsts)), [i for i in lsts if len(i) == max(map(len, lsts))]



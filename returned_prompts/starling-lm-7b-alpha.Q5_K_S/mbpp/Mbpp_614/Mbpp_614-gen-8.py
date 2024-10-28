
def cummulative_sum(tuples: list) -> int:
  total_sum = 0
  for i in tuples:
    total_sum += sum(i)
  return total_sum



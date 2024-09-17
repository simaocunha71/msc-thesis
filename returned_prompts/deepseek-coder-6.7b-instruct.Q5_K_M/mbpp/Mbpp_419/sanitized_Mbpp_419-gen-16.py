def round_and_sum(lst):
  rounded = [round(x) for x in lst]
  return sum(rounded) * len(rounded)
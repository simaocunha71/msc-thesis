def sum_range_list(lst, start, end):
  return sum(lst[start:end+1])  # note: end is exclusive in slicing, so we add 1 to include it
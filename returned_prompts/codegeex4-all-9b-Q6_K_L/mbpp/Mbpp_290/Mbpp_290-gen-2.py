def max_length(lst: list) -> tuple:
  max_len = max(len(sublist) for sublist in lst)
  max_sublist = [sublist for sublist in lst if len(sublist) == max_len]
  return max_len, max_sublist


def max_val(lst: list) -> int:
  max_num = max([x for x in lst if isinstance(x, int)])
  return max_num


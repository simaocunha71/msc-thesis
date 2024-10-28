def is_undulating(num: int) -> bool:
  return num > 0 and str(num) == "".join(sorted(str(num)))
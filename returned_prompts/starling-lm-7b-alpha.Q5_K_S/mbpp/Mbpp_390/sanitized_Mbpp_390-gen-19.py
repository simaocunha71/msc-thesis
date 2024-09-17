def add_string(nums: list, fmt_str: str) -> list:
  return [fmt_str.format(x) for x in nums]